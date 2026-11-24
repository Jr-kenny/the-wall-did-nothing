#!/usr/bin/env python3
"""Entry program for make.fun u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990.

Writes the one-star cat review to /output/entry.txt. Python 3, stdlib only.
The review is one line, 126 characters, and the program checks that before
writing anything, then reads the file back and confirms an exact match.
"""
import os
import sys

LINE = "One star. He calls me his baby, then locks the door and leaves for work. I screamed at the wall for six hours. It did nothing."

MIN_CHARS = 1
MAX_CHARS = 200
EXPECTED_CHARS = 126
FILENAME = "entry.txt"

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def fail(message):
    """Print the problem to stderr and stop with a nonzero exit code."""
    print("error: " + message, file=sys.stderr)
    raise SystemExit(1)


def check_line(line):
    """Gate checks: the entry must be one line of 1 to 200 characters."""
    if not isinstance(line, str):
        fail("entry must be text")
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        fail("line must be %d to %d characters, got %d" % (MIN_CHARS, MAX_CHARS, len(line)))
    if "\n" in line or "\r" in line:
        fail("line must be a single line, no line breaks allowed")
    if len(line) != EXPECTED_CHARS:
        fail("line must be %d characters, got %d" % (EXPECTED_CHARS, len(line)))
    if not line.startswith("One star."):
        fail("line must start with the one-star rating")
    if line != line.strip():
        fail("line must not start or end with whitespace")
    if "  " in line:
        fail("line must not contain double spaces")
    return line


def write_entry(line, out_dir):
    """Write the line to entry.txt inside out_dir and return the path."""
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, FILENAME)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    return out_path


def verify_entry(out_path, expected):
    """Read the file back and confirm it holds exactly the expected line."""
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != expected:
        fail("entry.txt does not match the line")
    if len(written) != len(expected):
        fail("entry.txt length does not match the line")
    return written


def main():
    line = check_line(LINE)
    out_path = write_entry(line, OUT_DIR)
    verify_entry(out_path, line)
    print("wrote %s (%d characters)" % (out_path, len(line)))


if __name__ == "__main__":
    main()
