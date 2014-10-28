#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Given a text file consisting of hex strings.
# Find strings which has been encrypted by single-character XOR

import sys
import singleByteXOR

def detect(cipher):
    (text, score, key) = singleByteXOR.attack(cipher)
    if score >= 200:
        print("Decrypted text:", text)
        if input("Good enough? (y for yes, else for no) ") == "y":
            print(cipher)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage:\t{} [path/]filename".format(sys.argv[0]))
        sys.exit()

    try:
        for line in open(sys.argv[1]):
            detect(line[:-1])
    except IOError:
        print("Couldn't open the file {}".format(sys.argv[1]))
