#!/usr/bin/python3
"""Create a function that writes text to a file and 
    reports how many characters it has written"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number of characters written."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
