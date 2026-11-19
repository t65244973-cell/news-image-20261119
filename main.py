"""Entry program for make.fun news-image-20261119.

Sums up the world's news of Thursday 19 November 2026 in one image.

The image is held in this repository as entry.png (a 1024x1024 PNG
newspaper front page). This program copies it, byte for byte, to
/output/entry.png. It uses only the Python standard library, reads
nothing from the network, and writes exactly the same bytes on every
run, so repeated runs are deterministic.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
DEST_DIR = "/output"
DEST = os.path.join(DEST_DIR, "entry.png")


def main() -> int:
    os.makedirs(DEST_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, DEST)
    print("wrote %s (%d bytes)" % (DEST, os.path.getsize(DEST)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
