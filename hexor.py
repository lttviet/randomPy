#!/usr/bin/python3
# -*- coding: utf-8 -*-
# xor 2 hex strings

import string

def isHex(s):
    '''Check if it is a hex string'''
    if (len(s) == 0 or len(s) % 2 != 0
                         or not all(c in string.hexdigits for c in s)):
        return False
    return True

def hexor(s1, s2):
    '''xor 2 hex strings, returning a hex string'''
    s3 = (int(c1,16) ^ int(c2,16) for (c1,c2) in zip(s1,s2))
    res = ""
    for c in s3:
        res += "{:x}".format(c)
    return res

if __name__ == "__main__":
    while True:
        s1 = input("First string:  ")
        s2 = input("Second string: ")
        if not isHex(s1) or not isHex(s2):
            print("Your hex string(s) are invalid!")
            continue
        else:
            print("Result:       ", hexor(s1,s2))
