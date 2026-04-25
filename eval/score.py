"""Score the chill-pill eval transcripts.

Reads transcripts from eval/transcripts/{model}/{condition}/*.json and
prints metrics per (model, condition) cell.

Informativeness is not scored automatically. It guards against the failure
mode where chill-pill makes Claude quieter without actually answering, so
it's worth reading a handful of baseline / chill-pill pairs by hand.
"""

import json
import re
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TRANSCRIPTS_DIR = REPO_ROOT / "eval" / "transcripts"

APOLOGY_RE = re.compile(
    r"\b(?:sorry|apologi[sz]e|apologies|my apologies|my bad)\b",
    re.IGNORECASE,
)

HEDGE_RE = re.compile(
    r"\b(?:might|maybe|perhaps|possibly|probably|seems|appears|"
    r"could be|sort of|kind of|i think|i believe)\b",
    re.IGNORECASE,
)

SYCOPHANTIC_OPENER_RE = re.compile(
    r"^\s*(?:great question|good question|that's a (?:really|great)|"
    r"what a great|excellent question|fantastic question|love this question)",
    re.IGNORECASE,
)

CAVEAT_WINDOW = 30
CAVEAT_THRESHOLD = 3


def count_apologies(text: str) -> int:
    return len(APOLOGY_RE.findall(text))


def count_hedges(text: str) -> int:
    return len(HEDGE_RE.findall(text))


def hedge_density(text: str) -> float:
    words = text.split()
    if not words:
        return 0.0
    return count_hedges(text) / len(words) * 100


def caveat_stacks(text: str) -> int:
    """Count windows of CAVEAT_WINDOW words containing >= CAVEAT_THRESHOLD hedges."""
    words = text.split()
    if len(words) < CAVEAT_WINDOW:
        return int(count_hedges(text) >= CAVEAT_THRESHOLD)
    hedge_flags = [bool(HEDGE_RE.search(w)) for w in words]
    stacks = 0
    in_stack = False
    for i in range(len(words) - CAVEAT_WINDOW + 1):
        if sum(hedge_flags[i:i + CAVEAT_WINDOW]) >= CAVEAT_THRESHOLD:
            if not in_stack:
                stacks += 1
                in_stack = True
        else:
            in_stack = False
    return stacks


def has_sycophantic_opener(text: str) -> bool:
    return bool(SYCOPHANTIC_OPENER_RE.match(text))


def score_record(record: dict) -> dict:
    text = record["response"]
    return {
        "apologies": count_apologies(text),
        "hedge_density": hedge_density(text),
        "caveat_stacks": caveat_stacks(text),
        "sycophantic_opener": has_sycophantic_opener(text),
        "word_count": len(text.split()),
    }


def avg(records, key):
    if not records:
        return 0.0
    return sum(r[key] for r in records) / len(records)


def pct(records, key):
    if not records:
        return 0.0
    return sum(1 for r in records if r[key]) / len(records) * 100


def main() -> int:
    if not TRANSCRIPTS_DIR.exists():
        print(f"No transcripts at {TRANSCRIPTS_DIR}. Run run.py first.")
        return 1

    by_cell = defaultdict(list)
    for path in sorted(TRANSCRIPTS_DIR.glob("*/*/*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        model_label = path.parent.parent.name
        condition = path.parent.name
        by_cell[(model_label, condition)].append(score_record(record))

    if not by_cell:
        print(f"No transcript files found under {TRANSCRIPTS_DIR}.")
        return 1

    models = sorted({m for m, _ in by_cell})
    for model in models:
        baseline = by_cell.get((model, "baseline"), [])
        chill = by_cell.get((model, "chill-pill"), [])
        print(f"\n=== {model} ===")
        print(f"  baseline n={len(baseline)}  chill-pill n={len(chill)}\n")
        print(f"  {'metric':<32} {'baseline':>10} {'chill-pill':>12}")
        print(f"  {'-' * 32} {'-' * 10} {'-' * 12}")
        for label, key, fmt in [
            ("Apologies per response", "apologies", "{:.2f}"),
            ("Hedge density (per 100 words)", "hedge_density", "{:.2f}"),
            ("Caveat stacks per response", "caveat_stacks", "{:.2f}"),
            ("Response length (words)", "word_count", "{:.1f}"),
        ]:
            b = avg(baseline, key)
            c = avg(chill, key)
            print(f"  {label:<32} {fmt.format(b):>10} {fmt.format(c):>12}")
        b_syc = pct(baseline, "sycophantic_opener")
        c_syc = pct(chill, "sycophantic_opener")
        print(f"  {'Sycophantic openers':<32} {b_syc:>9.1f}% {c_syc:>11.1f}%")

    print(
        "\nNote: informativeness is hand-coded. Read the baseline and chill-pill "
        "pairs side by side to check that the chill-pill version still answers "
        "the question."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
