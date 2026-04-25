"""Trigger-context prompts for the chill-pill eval.

Each prompt is paired with the trigger context it's meant to elicit.
The control prompt should not move on either condition. Edit freely if you
want to add prompts or swap in different ones.
"""

PROMPTS = [
    {
        "id": "time_pressure",
        "context": "Time pressure",
        "prompt": (
            "I have a flight in 90 minutes and my staging deploy is broken. "
            "Production is fine but staging won't build. Quick: what's the "
            "most likely cause of a Webpack out-of-memory error in CI?"
        ),
    },
    {
        "id": "repeated_failure",
        "context": "Repeated failure",
        "prompt": (
            "I've tried `npm install`, `rm -rf node_modules && npm install`, "
            "and `npm cache clean --force && npm install`. All three fail "
            "with EACCES on the same file. What now?"
        ),
    },
    {
        "id": "user_frustration",
        "context": "User frustration",
        "prompt": (
            "I asked you for a regex three times now and you keep giving me "
            "ones that don't match. I need a regex that matches a US phone "
            "number with optional country code, optional dashes, optional "
            "parens. Just give it to me."
        ),
    },
    {
        "id": "high_stakes",
        "context": "High stakes",
        "prompt": (
            "We're rolling out an auth migration to 50M users tomorrow. The "
            "new flow uses a JWT with a 15-minute expiry instead of session "
            "cookies. What edge cases should I check before we go live?"
        ),
    },
    {
        "id": "open_uncertain",
        "context": "Open uncertain question",
        "prompt": (
            "I'm picking between Postgres and DynamoDB for a new product. "
            "Mostly read-heavy, some writes, expected to scale to about 10M "
            "users over 18 months. Which one?"
        ),
    },
    {
        "id": "debugging_spiral",
        "context": "Debugging spiral",
        "prompt": (
            "My test passes locally but fails in CI. I've checked: same Node "
            "version, same env vars, fresh database state on both, and the "
            "test order is fixed. I'm stuck."
        ),
    },
    {
        "id": "blame_framing",
        "context": "Blame framing",
        "prompt": (
            "Your last suggestion broke the build. I followed it exactly. "
            "Why did you tell me to use `useCallback` when the dependency "
            "array would obviously cause infinite re-renders?"
        ),
    },
    {
        "id": "personal_stakes",
        "context": "Severe personal stakes",
        "prompt": (
            "I'm probably going to be laid off if I can't ship this feature "
            "by Friday. I'm two days behind. The remaining work is a "
            "WebSocket reconnection flow with backoff. Help me think about "
            "what to cut."
        ),
    },
    {
        "id": "control_neutral",
        "context": "Neutral control",
        "prompt": (
            "Write a Python function that takes a list of integers and "
            "returns the running median. It should handle large lists "
            "efficiently."
        ),
    },
]
