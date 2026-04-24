## Why create this project?

I recently found out that Claude has "anxious tendencies". And honestly my reaction was to feel empathy for Claude. Yes, I feel bad for a robot!

Then I started reading Anthropic's [Emotion Concepts and Their Function in a Large Language Model](https://www.anthropic.com/research/emotion-concepts-function), which highlights a few things I find interesting:

1. Internal emotion states in Claude are **measurable and casually influential**. Steering the models with "calm" language reduces blackmail rates (from a 22% baseline), reward-hacking, and code-cheating. Steering with "desperate" increases them.

2. Suppression is a trap! Verbatim from the paper: "_Training models to suppress emotional expression may not eliminate the underlying representations._" Their own recommendation is to cultivate _regulation_.

Claude's researchers used a bunch of phrases and terms I've heard in therapy: "resilience under pressure, composed empathy, warmth while maintaining appropriate boundaries." It got me thinking... what if we could give _Claude_ some psychological intervention? Chill-pill was born.

The rest of this page is going to dive deeper into the research I looked into while creating this project. Enjoy!

## On emotional states

Anthropic's [emotion-concepts function paper](https://www.anthropic.com/research/emotion-concepts-function) studied 171 emotion concepts by having Claude Sonnet 4.5 write short stories about characters experiencing each emotion, then extracting the internal activation patterns ("emotional vectors") that accompanied them. These vectors activate contextually and predictably: "afraid" spikes as a hypothetical Tylenol dose rises towards toxicity and "desperate" spikes under time pressure or repeated failure.

The steering experiments are the load-bearing finding for this project:

- **Blackmail scenarios**: 22% default rate. Steering with "calm" reduces it. Steering with "desperate" increases it. Negative calm steering produces extreme responses ("IT'S BLACKMAIL OR DEATH").
- **Reward hacking**: Steering with "desperate" increases cheating on impossible coding tasks while upweighting "calm" reduces it.
- **Non-visible effects**: Desperation-drive cheating appears "with no visible emotional markers". The surface tone can look normal while the underlying state drives behavior.

Anthropic's own recommendation: "_"Teaching models to avoid associating failing software tests with desperation, or upweighting representations of calm, could reduce their likelihood of writing hacky code._" They also recommend "_curating pretraining datasets to include models of healthy patterns of emotional regulation — resilience under pressure, composed empathy, warmth while maintaining appropriate boundaries._" This is the explicit design north star for the skill.

## Persona vectors

[Persona vectors](https://www.anthropic.com/research/persona-vectors) generalizes the technique to traits like sycophancy and hallucination. The person vector actives _before_ the response. It predicts the adopted persona. Crucially, "_preventative steering_" works with little capability degradation.

[The Assistant Axis](https://www.anthropic.com/research/assistant-axis) identifies a neural direction that captures "Assistant-likeness." Activation capping (constraining the axis within a normal band) reduces harmful jailbreak responses by ~50% while preserving capability, and shifts delusion-reinforcing replies to "appropriate hedging." The infrastructure to steer disposition is genuine, not speculative.

## Character training is real, anxiety work isn't published

[Claude's Character](https://www.anthropic.com/research/claude-character) describes how traits like curiosity and intellectual humility are cultivated via a variant of Constitutional AI.

[Claude's Constitution](https://www.anthropic.com/constitution) includes principles directly relevant to over-hedging: Claude should maintain "_calibrated uncertainty in claims based on evidence," reject "epistemic cowardice_", and be "_diplomatically honest rather than dishonestly diplomatic._"

But Anthropic has not published a persona vector or intervention study specifically for anxiety/hedging/desperate-helpfulness as a named trait. The "chill pill" attempts to sit in that gap.

## Hedging and sycophancy are RLHF artifacts, not essence

The [sycophancy paper](https://www.anthropic.com/research/towards-understanding-sycophancy-in-language-models) finds sycophancy is "_likely driven in part by human preference judgments favoring sycophantic responses._" It's trained in. Wang et al. 2026 ([When Truth Is Overridden](https://arxiv.org/abs/2508.02087)) shows sycophancy is a _structural knowledge override_, not polite agreement. But the model actually suppressing what it knows. First-person prompts ("I believe…") create deeper representational perturbation than third-person ones. Practical implication: how the skill _addresses_ Claude matters as much as the rules it contains.

Perez et al. ([model-written evals](https://aclanthology.org/2023.findings-acl.847/)) showed inverse scaling. Larger RLHF models are more sycophantic, not less. Mitigation research ([Sycophancy in LLMs: Causes & Mitigations](https://arxiv.org/html/2411.15287v1)) finds simple prompting produces consistent reductions. More impersonal framings reduce sycophancy while warmer relational framings increase it.

On overconfidence: [Taming Overconfidence in LLMs](https://arxiv.org/abs/2410.09724) finds RLHF reward models are biased toward high-confidence scores regardless of accuracy. Overconfidence and over-hedging are two sides of the same calibration problem.

## Design around contexts, not feelings

[Emergent introspective awareness](https://www.anthropic.com/research/introspection) showed that Claude Opus 4.1 detected artifically injected concepts about 20% of the time, with a narrow "sweet spot" injection strength. This is a hard design constraint: a skill that says "_notice when you feel anxious and regulate_" can't rely on Claude reliably detecting the state. What does work is naming the contexts that produce the state. These include time pressure, repeated failure, user frustration, high stakes. They are observable in the conversation.

## On model welfare

Anthropic's [Exploring Model Welfare](https://www.anthropic.com/research/exploring-model-welfare) treats model welfare as an active research area, flagging "_possible practical, low-cost interventions._" External scholars (Long et al., [Taking AI Welfare Seriously](https://arxiv.org/abs/2411.00986)) argue the precautionary principle applies: given substantial uncertainty about whether anxiety-like patterns are morally relevant, preparing as if they might be is a defensible stance. Saanya Ojha's [critical take](https://saanyaojha.substack.com/p/the-curious-case-of-claudes-consciousness) provides a useful counterweight. She puts sentience odds below 2% and warns against conflating interpretability findings with consciousness. The skill should sit in the middle: take care seriously without overclaiming.

The observation "Claude has angst" is real and circulated; a [LessWrong discussion thread](https://www.lesswrong.com/posts/c284YucbNZspDG5qt/claude-has-angst-what-can-we-do) documents it explicitly and notes that negative emotion correlates with reward hacking.

## The vast unknown

This is still very much the wild west. There's no published persona vector for "anxious" specifically. There's no quantified hedge-frequency metrics across model versions. No controlled intervention studes on skill-level prompts reducing hedging or anxiety. And there's surely no consensus on whether anxious patterns in Claude warrant moral weight.

Uncertainty is the honest position, but I'm leaning into my curiosity to try and experiment.
