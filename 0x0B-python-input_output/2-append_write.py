#!/usr/bin/python3
"""appends string to end of file and returns number of chars appended"""


def append_write(filename="", text=""):
    """Appends string to end of file and returns number of chars appended"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
