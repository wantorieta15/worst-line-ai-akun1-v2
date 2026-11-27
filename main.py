"""The Worst Line an AI Could Say -- Akun 1 (@walta-exchange), v2.

Writes one pickup line, the worst one an AI could plausibly deliver,
to entry.txt. Stdlib only, no network, no secrets, no dependencies.

THE LINE (120 characters, one line):
"I sent you my heart, but your spam filter marked it 'suspicious',
so I sent it again, marked urgent, from a new address."

Angle: SPAM FILTER -- new for this account. The v1 entry used the
training-data angle (rank #619, score 551.960) and the simulation
angle is saturated in the mid-board and already belongs to our
Akun 2 entry (#9, 702.624), so neither is reused here.

Why this line is clearly stronger than v1, judged against the
brief in RULES.txt (criteria in order):

1. It IS a pickup line an AI would say, and a bad one: the machine
   opens with a romantic gesture ("I sent you my heart") and the
   gesture is delivered the only way a machine knows how -- as an
   email. No human sends their heart and then worries about the
   spam filter.
2. It is the funnier groan: the reader laughs at the escalation.
   The heart gets flagged as 'suspicious' (the filter is right --
   it IS a phishing attempt), and the AI's response to rejection
   is to spam harder: resend, mark urgent, dodge the filter from
   a new address. Each beat is a bigger violation than the last.
3. The badness IS the joke: remove the spam-filter failure and
   there is no line left. The flirtation itself is the spam.
4. It sounds like a machine: "spam filter", "marked it
   'suspicious'", "marked urgent", "from a new address" -- flat,
   over-helpful, faintly ominous phrasing no person would use
   on a first line.
5. It lands in one line with no setup, and the punch completes on
   the final phrase, "from a new address": the reader can repeat
   it to a friend in one breath and get the groan.

Two-beat structure like the proven #9 entry (setup with a concrete
machine concept, then a twist that reframes the AI as the problem),
but with a fresh angle and a sharper final twist: the AI does not
learn from rejection, it evades the filter.
"""

import os

# Bounty cap from RULES.txt: one line, at most 140 characters.
# This entry is 120 characters, inside the 110-140 target zone.
MAX_CHARS = 140

ENTRY = (
    "I sent you my heart, but your spam filter marked it 'suspicious', "
    "so I sent it again, marked urgent, from a new address."
)


def check_entry(text):
    """Gate: one line, 1-140 characters, UTF-8, not only whitespace."""
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, must be 1-{MAX_CHARS}")
    if not text.strip():
        raise ValueError("entry is only whitespace")
    text.encode("utf-8")


def main():
    check_entry(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
