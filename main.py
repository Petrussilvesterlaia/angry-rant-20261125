#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest.

Writes one short, funny rant about a small everyday annoyance to
/output/entry.txt, validates it, and verifies it by reading it back.
"""

import os

RANT = (
    "Somebody in this house drank the last of the milk, left exactly one "
    "sip in the carton, and put it back in the fridge like a museum exhibit. "
    "One sip. Not enough for cereal, not enough for coffee, just enough to "
    "make me pour it and question every life choice that led me here. "
    "Finish it or admit it. Coward."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Validate: 1-400 characters, not only whitespace.
    if not RANT.strip():
        raise ValueError("Rant is empty or only whitespace.")
    if len(RANT) > 400:
        raise ValueError(f"Rant is {len(RANT)} characters, over the 400 limit.")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(RANT)

    # Verify: read the file back and confirm it matches exactly.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != RANT:
        raise ValueError("Verification failed: file contents do not match the rant.")
    if not (1 <= len(written) <= 400) or not written.strip():
        raise ValueError("Verification failed: file is invalid (length/whitespace).")

    print(f"Wrote {len(RANT)} characters to {OUTPUT_PATH}")
    print(f"Verified by read-back: {len(written)} characters, matches exactly.")


if __name__ == "__main__":
    main()
