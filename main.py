"""Real-Life Patch Notes: The Comedy Changelog.

Writes one patch note to /output/entry.txt.

The note follows the terse register of a real release note: a version
number, then a fix stated as if it shipped. The joke is the bug itself —
a brain that replays one embarrassing memory nightly, in surround sound.
"""

import os

ENTRY = (
    # The bug: the brain's 3 a.m. replay feature ships with no off switch,
    # and it always queues the single most embarrassing moment on file.
    "v2.4.1: fixed a bug where the brain replays your most embarrassing "
    "moment from 2009 every night at 3 a.m. in surround sound."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {path}: {ENTRY} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
