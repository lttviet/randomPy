#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Convert a hex string to base64 string

import base64
import string

def isHex(s):
    """
    Return True if s is a hex string, else False.
    A hex string has non-negative even length,
    and all characters belongs to string.hexdigits.
    """
    return (len(s) != 0 and len(s) % 2 == 0
                        and all(c in string.hexdigits for c in s))

def convert(string):
    """
    Convert a hex string to base64 string.
    """
    # turn hex string into byte string
    raw = bytes.fromhex(string)
    # encode byte string using Base64
    raw = base64.b64encode(raw)
    return raw.decode()

if __name__ == "__main__":
    while True:
        s = input("Enter a hex string: ")
        if not isHex(s):
            print("Your string is not a hex string.")
        else:
            print("The equivalent base64 string is: ", convert(s))
