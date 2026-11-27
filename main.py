"""Worst Line -- Akun 1 (@walta-exchange), v2 (reviser rewrite).

The bounty asks for the worst pickup line an AI could say: one line,
at most 140 characters, winner-take-all. This program emits exactly
one such line to ``entry.txt`` and nothing else. It uses only the
Python standard library, touches no network, reads no secrets, and
has no third-party dependency, so it runs identically on the grading
server and on any local machine.

THE LINE (120 characters, byte-identical across v2 builds):
    I sent you my heart, but your spam filter marked it 'suspicious',
    so I sent it again, marked urgent, from a new address.

ANGLE -- SPAM FILTER. The v1 entry for this account (training-data
angle) finished rank #619 with score 551.960, and the simulation
angle is already taken by our Akun 2 entry (rank #9, 702.624), so
both angles are retired here. The spam-filter angle is new for this
account and is the whole joke:

* The AI opens with a romantic gesture and delivers it the only way
  a machine knows how: as an email. No human sends their heart and
  then worries about the spam filter.
* The filter is right to flag the heart as 'suspicious' -- it IS a
  phishing attempt -- and the AI's answer to rejection is to spam
  harder: resend, mark urgent, dodge the filter from a new address.
  Every beat escalates the violation.
* The badness IS the joke. Strip the spam-filter failure out and no
  line is left: the flirtation itself is the spam.
* The diction is flat, over-helpful machine-speak no person would
  use as an opener: "spam filter", "marked it 'suspicious'",
  "marked urgent", "from a new address".
* The punch lands on the final phrase, "from a new address", so
  the line repeats cleanly in one breath and still gets the groan.

Structure mirrors the proven #9 entry (concrete machine concept as
setup, then a twist that reframes the AI as the problem), but the
twist here is sharper: the AI does not learn from rejection, it
evades the filter.
"""

import os
import sys

# --- Bounty limits (from RULES.txt) -------------------------------------
# One line, at most 140 characters. This entry is 120 characters,
# inside the 110-140 target zone the brief rewards.
MAX_CHARS = 140
MIN_CHARS = 1

# --- Output contract -----------------------------------------------------
# The grader reads <output dir>/entry.txt. The directory comes from
# MAKEFUN_OUTPUT_DIR and falls back to /output. The file is written
# directly (plain open + explicit chmod 0o644): no temporary file and
# no os.replace, so the grader can always read it.
OUTPUT_FILENAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_MODE = 0o644

# --- The entry -----------------------------------------------------------
# Single literal, one line, exactly 120 characters. Do not reword,
# re-punctuate, or re-wrap: the graded text is this string plus one
# trailing newline in entry.txt.
# Revision pass (submitter, 27 Nov 2026): entry text verified
# byte-identical after the full rewrite (sha256 entry.txt eebc4ef8...);
# this comment only, no wording change.
ENTRY = (
    "I sent you my heart, but your spam filter marked it 'suspicious', "
    "so I sent it again, marked urgent, from a new address."
)


# --- Validation ----------------------------------------------------------
class EntryError(ValueError):
    """Raised when the entry breaks any bounty rule."""


def _check_single_line(text):
    if "\n" in text or "\r" in text:
        raise EntryError("entry must be a single line, no line breaks")


def _check_length(text):
    size = len(text)
    if size < MIN_CHARS or size > MAX_CHARS:
        raise EntryError(
            "entry is %d characters, must be %d-%d" % (size, MIN_CHARS, MAX_CHARS)
        )


def _check_not_blank(text):
    if not text.strip():
        raise EntryError("entry is only whitespace")


def _check_encodable(text):
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise EntryError("entry is not encodable as UTF-8: %s" % exc)


def validate_entry(text):
    """Run every bounty gate on the entry text, in order."""
    for check in (_check_single_line, _check_length, _check_not_blank, _check_encodable):
        check(text)


# --- Output --------------------------------------------------------------
def resolve_output_dir():
    """Output directory from the environment, with the /output fallback."""
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR
    return chosen


def output_path(out_dir):
    return os.path.join(out_dir, OUTPUT_FILENAME)


def write_entry(path, text):
    """Write the entry plus one trailing newline, world-readable."""
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
        handle.write("\n")
    os.chmod(path, OUTPUT_MODE)


def main(argv=None):
    validate_entry(ENTRY)
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    write_entry(output_path(out_dir), ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
