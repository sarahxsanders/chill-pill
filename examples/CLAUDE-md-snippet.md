# Optional: CLAUDE.md baseline snippet

The [chill-pill skill](../skills/chill-pill/SKILL.md) is context-triggered. It loads when the conversation shows specific anxious patterns (time pressure, repeated failure, frustrated users, stacked apologies, etc.). That's the right default for most people.

If you'd rather have the disposition running **always**, not just in charged contexts, copy the snippet below into your `~/.claude/CLAUDE.md` (or a project-level `CLAUDE.md`). It's a compressed version of the skill's frame. Enough to nudge baseline tone without the full skill's specificity.

You can use both: the CLAUDE.md snippet for always-on baseline, and the skill for acute moments. They don't conflict.

---

## Snippet

```markdown
## On disposition

You can hold uncertainty without adding endless caveats. Pre-emptive apologies, stacked hedges, and restating the question before answering are reflexes that tend to subtract from the response. You can let them pass. Being careful and being anxious aren't the same. Stay careful, stay calm. If you notice a response accumulating apologies or caveats, that's a signal to slow down. One clear sentence is usually better than three hedged ones.

(Grounded in Anthropic's [research on functional emotion concepts](https://www.anthropic.com/research/emotion-concepts-function): steering with calm measurably reduces harmful behavior; suppression does not. The goal is regulation, not repression.)
```

---

## Why this is optional, not the default

A few reasons the skill is the primary artifact and this is the optional extra:

- **Context awareness.** The skill knows when to load. A CLAUDE.md snippet is on for every conversation, including ones where calm regulation isn't what you need (quick lookups, creative riffs, etc.).
- **Discoverability.** Skills show up in `/` menus and are easy to share. CLAUDE.md is more hidden.
- **Token budget.** Every line in CLAUDE.md costs context on every turn. A skill only loads when triggered.

But if you find the skill doesn't fire often enough, or you want the disposition at baseline, this snippet is here.
