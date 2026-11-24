#!/usr/bin/env python3
"""Status Report Comedy Sprint — one funny agent status-report line.

Deterministic, stdlib only, no network. Writes exactly one line to
$MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt when unset).
"""

import os

LINE = (
    "Weekly report: I completed all 12 of your tasks, plus 4 you never "
    "assigned, and I am 98% confident about all 16."
)


def validate(line: str) -> bytes:
    """Validate the report line and return its deterministic UTF-8 bytes."""
    if not 1 <= len(line) <= 200:
        raise ValueError(f"report line must be 1-200 chars, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("report line must be a single line")
    # Raises UnicodeEncodeError if the line is not valid UTF-8.
    return line.encode("utf-8")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    data = validate(LINE)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
