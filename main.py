#!/usr/bin/env python3
"""One-line pitches — a make.fun entry.

The program writes one sentence to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt): a pitch meant to convince a friend who
has never coded to let an AI agent build their first app idea on
make.fun. The sentence is 72 characters, inside the competition's gate
of 1 to 240 characters of UTF-8 text. Standard library only, no
network, and deterministic: the same bytes on every run.
"""

import os

LINE = "Alarms, but they're disappointed in you — snooze now costs self-respect."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # The entry file holds exactly the one sentence: no trailing newline,
    # so the text the judge reads is the sentence itself, byte for byte.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
