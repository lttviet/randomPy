#!/usr/bin/python3
# -*- coding: utf-8 -*-
# xor 2 equal-length hex strings

import util

def hexor(s1, s2):
    """
    XOR 2 hex strings, returns a hex string.
    """
    return "{:02x}".format(util.xor(s1,s2,16,16))

if __name__ == "__main__":
    while True:
        s1 = input("First hex string:  ")
        s2 = input("Second hex string: ")
        if not util.isHex(s1) or not util.isHex(s2):
            print("Your hex string(s) are invalid!")
        else:
            print("Result: ", hexor(s1,s2))
