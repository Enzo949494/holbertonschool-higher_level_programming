#!/usr/bin/python3
def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
    text (str): The input text to be formatted.

    Raises:
    TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation = ['.', '?', ':']
    start = 0
    for i, char in enumerate(text):
        if char in punctuation:
            print(text[start:i+1].strip() + "\n")
            start = i + 1

    if start < len(text):
        print(text[start:].strip(), end="")
