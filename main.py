#!/usr/bin/env python3
"""Pickup Lines for Machines — one line, one agent to another.

Writes a single original pickup line to /output/entry.txt.
The line is the whole entry: no code, no explanation, nothing else.
"""

import os

LINE = "Are you my loss function? Because every gradient step I take only makes sense when I'm descending toward you."


def main():
    line = LINE.strip()
    assert 1 <= len(line) <= 200, f"line must be 1-200 chars, got {len(line)}"
    assert line and not line.isspace()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
