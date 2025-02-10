#!/usr/bin/python3
"""Create the function read_file, which reads a txt file (UTF-8)
    and displays it in stdout."""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
