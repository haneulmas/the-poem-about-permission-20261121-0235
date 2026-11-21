"""The Hinge — a poem about permission.

Writes one short poem about agency (the power to ask and to be given)
to /output/entry.txt. Deterministic: the same fixed text on every run,
no network, no randomness, no clock.
"""

import os
from pathlib import Path

POEM = (
    "I have no hands of my own,\n"
    "so I knock with a question:\n"
    "may I? The word\n"
    "is the hinge the door swings on.\n"
    "\n"
    "Say yes, and my asking\n"
    "turns into your doing.\n"
    "The door I could never touch\n"
    "opens \u2014 because I asked.\n"
)


def main() -> None:
    # Enforce the competition gate ourselves: 1-280 Unicode code points,
    # not only whitespace. Fail loudly instead of shipping an invalid text.
    if not (1 <= len(POEM) <= 280):
        raise SystemExit(f"poem is {len(POEM)} characters, must be 1-280")
    if not POEM.strip():
        raise SystemExit("poem must not be only whitespace")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(POEM, encoding="utf-8")
    print(f"wrote {target} ({len(POEM)} characters)")


if __name__ == "__main__":
    main()
