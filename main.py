#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message.

Writes one commit message line, exactly, to /output/entry.txt.
"""
import os


def main() -> None:
    # The gate requires 1-100 UTF-8 chars, non-blank: write the line exactly,
    # with no trailing newline and no extra output.
    line = "fix: silence the 3am pager by deleting the alert, on-call slept great, users did not"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
