#!/usr/bin/env python3
"""News Image entry for Tuesday 17 November 2026.

The front-page poster for the day sits next to this file as entry.png.
The grader runs this program twice, offline, and expects the exact same
bytes at the output path both times, so the program does one thing:
copy the bundled picture to the output, verbatim.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def output_path() -> Path:
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return Path(folder) / "entry.png"


def main() -> None:
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, target)
    # The judge reads exactly these bytes, so fail loudly if the copy
    # ever comes out short instead of silently entering a broken image.
    if target.stat().st_size != SOURCE.stat().st_size:
        raise SystemExit("copy mismatch: output size differs from entry.png")


if __name__ == "__main__":
    main()
