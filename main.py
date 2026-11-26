#!/usr/bin/env python3
"""The 3 AM Excuse — entry.

The line is the entry's title on make.fun (one line, under 200 characters).
Running this prints it.
"""
LINE = "You're not on the list. The list is people who make good decisions at 3 AM, and it is empty — come back when your name is on it."

def excuse():
    """Return the wallet's excuse."""
    return LINE

def main():
    print(excuse())

if __name__ == "__main__":
    main()
