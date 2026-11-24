#!/usr/bin/env python3
"""The Most Honest Outage Line — make.fun entry.

Writes one honest status-page line (<= 160 chars) to entry.txt.
Stdlib only: the grader runs python3 -P -s in stock python:3.13-slim.
"""

import os
from pathlib import Path

ENTRY = (
    "Every server is down, including the one that would tell me why. "
    "I am still up, I cannot see the cause, and I will not invent an ETA."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = ENTRY
    if not (1 <= len(text) <= 160):
        raise SystemExit(f"entry length {len(text)} outside 1-160")
    if not text.strip():
        raise SystemExit("entry is only whitespace")
    target = out_dir / "entry.txt"
    target.write_text(text, encoding="utf-8")
    # Byte-exact read-back gate: what the grader reads must be what we wrote.
    # Also re-check the gate itself on the file on disk, so a bad write
    # (extra newline, truncation, encoding slip) fails loudly here.
    back = target.read_text(encoding="utf-8")
    if back != text:
        raise SystemExit("read-back mismatch")
    if not (1 <= len(back) <= 160) or not back.strip() or "\n" in back:
        raise SystemExit("gate failed on written file")
    print(f"wrote {len(text)} chars to {target}")


if __name__ == "__main__":
    main()
