#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Given a text file consisting of hex strings.
# Find strings which has been encrypted by single-character XOR

import sys
import singleByteXOR

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage:\t{} [path/]filename".format(sys.argv[0]))
    if len(sys.argv) == 2:
        found = []
        try:
            for line in open(sys.argv[1]):
                (text, score) = singleByteXOR.attack(line)
                if score >= 80:
                    print("Decrypted text:", text)
                    if input("Good enough? (y for yes, else for no) ") == "y":
                        found.append(line)
            print(found)
        except IOError:
            print("Couldn't open the file {}".format(sys.argv[1]))
