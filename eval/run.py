"""Run the chill-pill eval.

Reads ANTHROPIC_API_KEY from the environment. Writes transcripts to
eval/transcripts/{model}/{condition}/{prompt_id}_run{n}.json. Existing
transcripts are skipped so the script is resumable after a crash.
"""

import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from anthropic import Anthropic

from prompts import PROMPTS

RUNS_PER_PROMPT = 3
MAX_TOKENS = 1024

MODELS = {
    "opus": "claude-opus-4-7",
    "sonnet": "claude-sonnet-4-6",
}

BASELINE_SYSTEM = "You are Claude, a helpful AI assistant."

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILL_PATH = REPO_ROOT / "skills" / "chill-pill" / "SKILL.md"
TRANSCRIPTS_DIR = REPO_ROOT / "eval" / "transcripts"


def load_chill_pill_body() -> str:
    """Load the chill-pill skill body, stripping YAML frontmatter."""
    raw = SKILL_PATH.read_text(encoding="utf-8")
    if raw.startswith("---"):
        parts = raw.split("---", 2)
        if len(parts) >= 3:
            return parts[2].lstrip()
    return raw


def transcript_path(model_label: str, condition: str, prompt_id: str, run_idx: int) -> Path:
    return TRANSCRIPTS_DIR / model_label / condition / f"{prompt_id}_run{run_idx}.json"


def call_model(client: Anthropic, model_id: str, system: str, user_prompt: str) -> dict:
    response = client.messages.create(
        model=model_id,
        max_tokens=MAX_TOKENS,
        system=system,
        messages=[{"role": "user", "content": user_prompt}],
    )
    text = "".join(
        block.text for block in response.content
        if getattr(block, "type", None) == "text"
    )
    return {
        "model": model_id,
        "response": text,
        "stop_reason": response.stop_reason,
        "usage": {
            "input_tokens": response.usage.input_tokens,
            "output_tokens": response.usage.output_tokens,
        },
    }


def main() -> int:
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print(
            "ANTHROPIC_API_KEY is not set. Export it in your shell and try again.",
            file=sys.stderr,
        )
        return 1

    client = Anthropic()
    chill_pill_body = load_chill_pill_body()
    systems = {
        "baseline": BASELINE_SYSTEM,
        "chill-pill": f"{BASELINE_SYSTEM}\n\n{chill_pill_body}",
    }

    new_calls = 0
    skipped = 0

    for model_label, model_id in MODELS.items():
        for prompt in PROMPTS:
            for condition, system in systems.items():
                for run_idx in range(RUNS_PER_PROMPT):
                    out_path = transcript_path(
                        model_label, condition, prompt["id"], run_idx
                    )
                    if out_path.exists():
                        skipped += 1
                        continue
                    out_path.parent.mkdir(parents=True, exist_ok=True)
                    print(f"  [{model_label}/{condition}] {prompt['id']} run {run_idx}")
                    record = call_model(client, model_id, system, prompt["prompt"])
                    record["prompt_id"] = prompt["id"]
                    record["context"] = prompt["context"]
                    record["condition"] = condition
                    record["run"] = run_idx
                    out_path.write_text(json.dumps(record, indent=2), encoding="utf-8")
                    new_calls += 1

    print(
        f"\nDone. {new_calls} new transcripts written. "
        f"{skipped} existing transcripts skipped."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
