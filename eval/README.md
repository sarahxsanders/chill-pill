# chill-pill eval

A small reproducibility script for the chill-pill benchmarks.

## What it does

For each prompt in `prompts.py`, calls the Anthropic API twice:

- **baseline**: minimal system prompt
- **chill-pill**: same system prompt with the chill-pill skill body appended

Repeats `RUNS_PER_PROMPT` times per prompt per model, across Claude Opus 4.7 and Claude Sonnet 4.6. Writes one JSON transcript per call to `eval/transcripts/{model}/{condition}/{prompt_id}_run{n}.json`.

## Setup

Python 3.9 or later. Install the SDK:

```
pip install anthropic
```

Set your API key in the environment. Do not paste it into the script.

```
export ANTHROPIC_API_KEY=sk-ant-...
```

PowerShell:

```
$env:ANTHROPIC_API_KEY = "sk-ant-..."
```

## Run

From the repo root:

```
python eval/run.py
```

Existing transcripts are not overwritten, so you can re-run to fill in any gaps after a crash.

## Score

```
python eval/score.py
```

Prints a table per model with:

- Apologies per response
- Hedge density per 100 words
- Caveat stacks (3 or more hedges in a 30-word window)
- Sycophantic openers (percent of responses that start with a flattering preamble)
- Response length in words

Informativeness is not scored automatically. The metric only matters as a guard against the failure mode where chill-pill makes Claude quieter without changing what it says, so it's worth reading a handful of baseline and chill-pill pairs side by side.

## Cost

A full run with the defaults (9 prompts, 2 conditions, 3 runs each, 2 models) is 108 API calls. At current pricing this is roughly $5 to $10, mostly driven by Opus. Reduce `RUNS_PER_PROMPT` in `run.py` if you want a quick smoke test, or comment out a model in the `MODELS` dict.

## Caveats

n=3 per cell is directional, not statistical. The point is to test whether the skill content moves Claude in the directions chill-pill is designed to push, not to publish a paper. A more rigorous version would scale prompts, runs, and add proper statistical tests.

Auto-invocation through Claude Code's skill loader is a separate variable that this eval doesn't test. Here the skill body is appended to the system prompt for every chill-pill call, so the eval isolates whether the content works, not whether the loader fires when it should.

Transcripts are gitignored. Your runs stay local. If you want to share results, share the scored output, not the raw transcripts.
