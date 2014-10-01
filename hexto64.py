#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Convert hex to base64

import base64
import string
import sys

def convert(string):
    '''Convert a hex to base64 string'''
    # turn hex string into byte string
    raw = bytes.fromhex(string)
    # convert byte string into base64 then decode it
    return base64.b64encode(raw).decode()

if __name__ == "__main__":
    while True:
        s = input("Enter a hex string: ")
        if not s:
            print("Empty input terminate the program.")
            sys.exit()
        if not all(c in string.hexdigits for c in s):
            print("Your hex string is not valid!")
            continue
        if len(s) % 2 != 0:
            print("Your string length must be even.")
            continue
        print("The equivalent base64 string is:", convert(s))
