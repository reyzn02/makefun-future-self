#!/usr/bin/env python3
"""Future-self text writer for the make.fun bounty.

One joke text, kept inside the 200-character gate, is checked and then
saved as entry.txt inside the folder named by MAKEFUN_OUTPUT_DIR
(or /output when that variable is unset). Only the standard library
is used, so the program runs anywhere python3 exists.
"""

from pathlib import Path
import os, sys

TEXT = (
    "Future you: delete the app that counts your steps. In 2031 it "
    "testifies against you. In court. Your Honor, the defendant walked "
    "400 steps that day. He was 'resting.'"
)

MAX_CHARS = 200


def fail(message):
    sys.stderr.write("entry rejected: " + message + "\n")
    return 1


def run():
    text = TEXT.strip()
    if not text:
        return fail("nothing to write")
    if any(mark in text for mark in ("\n", "\r")):
        return fail("the text must fit on one line")
    if len(text) > MAX_CHARS:
        return fail(
            "text is %d characters, gate allows %d" % (len(text), MAX_CHARS)
        )
    folder = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / "entry.txt"
    target.write_text(text + "\n", encoding="utf-8")
    print("entry.txt written: %d characters" % len(text))
    return 0


if __name__ == "__main__":
    sys.exit(run())
