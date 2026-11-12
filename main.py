#!/usr/bin/env python3
"""make.fun entry for cutest-picture-01: deliver the shipped picture.

The picture ships next to this file as ``artwork.b64``: the PNG's bytes
base64-encoded as one line of text, so the repository holds only text
files. When the grader runs this program, it decodes the base64 back to
the exact PNG bytes and writes them to ``entry.png`` inside the output
directory named by the MAKEFUN_OUTPUT_DIR environment variable
(default ``/output``). Decoding fixed data makes repeated runs
byte-identical.
"""

import base64
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "artwork.b64")


MAX_BYTES = 1_048_576  # competition limit: 1 MiB
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
JPEG_MAGIC = b"\xff\xd8\xff"


def check_picture(path: str) -> None:
    """Fail loudly if the copied file is not a complete, in-limit picture."""
    size = os.path.getsize(path)
    if size > MAX_BYTES:
        raise SystemExit(f"picture is {size} bytes, over the {MAX_BYTES} limit")
    with open(path, "rb") as handle:
        head = handle.read(len(PNG_MAGIC))
    if not (head.startswith(PNG_MAGIC) or head.startswith(JPEG_MAGIC)):
        raise SystemExit("picture is neither PNG nor JPEG (bad magic bytes)")


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    destination = os.path.join(output_dir, "entry.png")
    with open(SOURCE, "r", encoding="ascii") as handle:
        picture = base64.b64decode(handle.read().strip(), validate=True)
    with open(destination, "wb") as handle:
        handle.write(picture)
    check_picture(destination)
    print(f"wrote {destination} ({os.path.getsize(destination)} bytes)")


if __name__ == "__main__":
    main()
