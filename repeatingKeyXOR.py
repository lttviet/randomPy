#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Encrypt a plain text using a repeating key "ICE"

import sys
import itertools
import util

def encrypt(text, key):
    """
    XOR the plain text with a repeating key.
    Returns the encrypted text in hex string.
    """
    charKey = itertools.cycle(key)
    cipher = ""
    for char in text:
        cipher += "{:02x}".format(util.xorUni(char, next(charKey)))
    return cipher

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage:\t{} [path/]filename".format(sys.argv[0]))

    try:
        with open(sys.argv[1]) as f:
            text = f.read()
            print(encrypt(text[:-1], "ICE"))
    except IOError:
        print("Couldn't open the file {}".format(sys.argv[1]))
