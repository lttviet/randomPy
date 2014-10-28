#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Convert a hex string to base64 string

import base64
import util

def hexTo64(string):
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
        if not util.isHex(s):
            print("Your string is not a hex string.")
        else:
            print("The equivalent base64 string is: ", hexTo64(s))
