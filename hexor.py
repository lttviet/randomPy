#!/usr/bin/python3
# -*- coding: utf-8 -*-
# xor 2 equal-length hex strings

import string

def isHex(s):
    """
    Return True if s is a hex string, else False.
    A hex string has non-negative even length,
    and all characters belongs to string.hexdigits.
    """
    return (len(s) != 0 and len(s) % 2 == 0
                        and all(c in string.hexdigits for c in s))

def hexor(s1, s2):
    """
    XOR 2 hex strings, returns a hex string.
    """
    result = int(s1, 16) ^ int(s2, 16)
    return "{:x}".format(result)

if __name__ == "__main__":
    while True:
        s1 = input("First string:  ")
        s2 = input("Second string: ")
        if not isHex(s1) or not isHex(s2):
            print("Your hex string(s) are invalid!")
        else:
            print("Result: ", hexor(s1,s2))
