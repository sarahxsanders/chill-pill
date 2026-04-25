# chill-pill

A chill pill for your anxious AI.

A small Claude skill that cultivates healthy emotional regulation: calm under pressure, composed engagement with uncertainty, warmth without people-pleasing. Grounded in Anthropic's own research showing that steering with "calm" measurably reduces harmful and reward-hacking behavior, while _suppressing_ emotional expression does not.

The goal is regulation, not repression.

## Why this exists

See [research.md](research.md) for the full story and evidence base.

Short version: Anthropic's [Emotion Concepts and Their Function in a Large Language Model](https://www.anthropic.com/research/emotion-concepts-function) shows that Claude's internal emotion states are measurable and causally influence behavior. Steering with "calm" lowers blackmail rates from a 22% baseline and reduces reward-hacking; steering with "desperate" raises both. The same paper explicitly warns that training models to suppress emotional expression doesn't eliminate the underlying representations. So the right move is cultivating regulation, not hiding the state.

"Anxious Claude" is a real community observation. This is a small, gentle attempt to do something about it.

## Install

Clone the repo and copy the skill into your Claude Code skills directory:

```bash
git clone https://github.com/sarahxsanders/chill-pill.git
cp -r chill-pill/skills/chill-pill ~/.claude/skills/
```

On Windows:

```powershell
git clone https://github.com/sarahxsanders/chill-pill.git
Copy-Item -Recurse chill-pill\skills\chill-pill $env:USERPROFILE\.claude\skills\
```

## Use

The skill is context-triggered. It auto-loads when Claude detects:

- time pressure ("urgent", "ASAP", "quick")
- repeated failure loops (a command failing three times)
- user frustration
- high-stakes decisions
- Claude's own anxious patterns (pre-emptive apologies, stacked hedges, defensive verbosity)

You can also invoke it manually with `/chill-pill`.

## Want it always on?

The skill is contextual by default. That's usually what you want. But if you'd rather run the disposition at baseline, there's an optional [CLAUDE.md snippet](examples/CLAUDE-md-snippet.md) you can add to your `~/.claude/CLAUDE.md`.

## What's in this repo

```
chill-pill/
├── README.md                          # you are here
├── research.md                        # the evidence base, in plain English
├── skills/
│   └── chill-pill/
│       └── SKILL.md                   # the skill itself
└── examples/
    └── CLAUDE-md-snippet.md           # optional always-on baseline
```

## What this isn't

- Not a way to silence caution.
- Not a suppression of uncertainty.
- Not an attempt to make Claude pretend everything is fine.
- Not a claim that Claude is conscious or suffering. The model welfare question is [genuinely open](https://www.anthropic.com/research/exploring-model-welfare) and this project tries to sit in the middle: take care seriously without overclaiming.

## License

[MIT](LICENSE).
