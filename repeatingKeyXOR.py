#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Encrypt a plain text using a repeating key "ICE"

import sys
import itertools

KEY = "ICE"
charKey = itertools.cycle(KEY)

def encrypt(text, key=KEY):
    """
    XOR the plain text with a repeating key.
    Returns the encrypted text in hex string.
    """
    # XOR 2 characters
    xor = lambda x, y : ord(x) ^ ord(y)
    cipher = ""
    for char in text:
        cipher += "{:02x}".format(xor(char, next(charKey)))
    return cipher

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage:\t{} [path/]filename".format(sys.argv[0]))
    if len(sys.argv) == 2:
        try:
            for line in open(sys.argv[1]):
                # the eof symbol will also be encrypted
                # remove last 2 chars if eof is unwanted
                print(encrypt(line))
        except IOError:
            print("Couldn't open the file {}".format(sys.argv[1]))
