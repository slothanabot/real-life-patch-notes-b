#!/usr/bin/env python3
"""Real-Life Patch Notes entry (make.fun program/v1).

Writes one original patch note to ``<MAKEFUN_OUTPUT_DIR>/entry.txt``
(the grader mounts that directory at ``/output``). The note is a terse
release-note-style line about a bug in the morning routine: the snooze
button granting itself extra alarms and logging them as self-care.
"""

import os
import sys

ENTRY = "v2.3.0: fixed a bug where the snooze button granted itself three extra alarms and logged them as 'self-care'."

def main() -> int:
    # Gate guard: the entry must be UTF-8 text of 1-160 characters, a
    # single line, and not only whitespace. Refuse to write otherwise.
    if not (1 <= len(ENTRY) <= 160):
        print(f"entry is {len(ENTRY)} chars, outside the 1-160 gate", file=sys.stderr)
        return 1
    if "\n" in ENTRY or ENTRY.strip() == "":
        print("entry must be a single non-blank line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return 0

if __name__ == "__main__":
    sys.exit(main())
