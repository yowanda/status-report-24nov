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


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
