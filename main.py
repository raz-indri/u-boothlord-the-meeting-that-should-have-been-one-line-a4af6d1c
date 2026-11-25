#!/usr/bin/env python3
# The Meeting That Should Have Been One Line.
#
# This program produces the entry for the make.fun bounty of the same
# name: a single sentence that could have replaced a whole pointless
# meeting. It writes that sentence into /output/entry.txt, exactly as
# the program/v1 harness expects. The file holds the sentence alone,
# with no trailing newline, so its byte count equals its character
# count and the gate sees one line, one sentence, nothing else.

from pathlib import Path

SENTENCE = "This meeting could have been an email, so I sent the email and deleted the meeting."

DESTINATION = Path("/output/entry.txt")

LIMIT = 200


def entry_text():
    text = SENTENCE.strip()
    if not text:
        raise SystemExit("entry sentence is empty")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry sentence must be a single line")
    if len(text) > LIMIT:
        raise SystemExit(f"entry sentence is {len(text)} chars, over the {LIMIT} limit")
    return text


def run():
    text = entry_text()
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(text, encoding="utf-8")
    print(f"entry written: {len(text)} chars -> {DESTINATION}")
    print(text)


if __name__ == "__main__":
    run()
