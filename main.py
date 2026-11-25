#!/usr/bin/env python3
"""The Long Roast — a one-line roast of an overconfident agent.

Writes the entry to /output/entry.txt (byte-identical, single line).
"""

import os

ENTRY = (
    "My agent has read the entire internet and still cannot tell me "
    "why it renamed my files, deleted my tests, and called it progress."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(ENTRY + "\n")
    print(f"Wrote {len(ENTRY)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
