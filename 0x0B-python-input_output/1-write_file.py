#!/usr/bin/python3
"""writes a string and returns the number of characters"""


def write_file(filename="", text=""):
    """counts the characters of a string"""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
