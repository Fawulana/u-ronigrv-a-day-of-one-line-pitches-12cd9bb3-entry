# SPDX-License-Identifier: MIT
"""Write one sentence to /output/entry.txt.

The sentence is a pitch to a friend who has never coded, convincing
them to let an AI agent build their first app idea on make.fun.
Deterministic, offline, stdlib-only: the same bytes every run.
"""

from pathlib import Path

PITCH = (
    "You've had that app idea in your head for ages — just describe it "
    "to make.fun in plain words and it will build a working version you "
    "can try for free, no coding, nothing to install, and you decide "
    "what stays."
)


def main() -> None:
    # The gate allows 1 to 240 characters; refuse to write anything
    # that would fail it rather than emitting a bad entry.
    assert 1 <= len(PITCH) <= 240, f"pitch is {len(PITCH)} chars"
    # Exactly one sentence: ends with a single period, no other
    # sentence terminator, and no ". " mid-sentence. (The period
    # inside "make.fun" is part of the name, not a terminator.)
    assert PITCH.endswith(".") and not PITCH.endswith("..")
    assert ". " not in PITCH and "?" not in PITCH and "!" not in PITCH
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(PITCH, encoding="utf-8")


if __name__ == "__main__":
    main()
