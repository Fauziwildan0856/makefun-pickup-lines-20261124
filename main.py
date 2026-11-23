"""Pickup Lines for Machines — entry program.

Writes the one pickup line one AI agent would send another AI agent
to entry.txt in the output directory, then reads it back to verify
it is exactly the intended text and within the 1-200 character gate.
Standard library only.
"""

import os
import sys

ENTRY_TEXT = (
    "Do you believe in love at first ping, "
    "or should I retry with exponential backoff?"
)


def main():
    output_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY_TEXT)
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != ENTRY_TEXT:
        sys.stderr.write("entry.txt does not match the intended text\n")
        return 1
    if not written.strip():
        sys.stderr.write("entry.txt is only whitespace\n")
        return 1
    if not 1 <= len(written) <= 200:
        sys.stderr.write("entry.txt length %d outside 1-200 characters\n" % len(written))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
