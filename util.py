#!/usr/bin/python3
# -*- coding: utf-8 -*-

import string
import base64

def isHex(s):
    """
    Return True if s is a hex string, else False.
    A hex string has non-negative even length,
    and all characters belongs to string.hexdigits.
    """
    return (len(s) > 0 and len(s) % 2 == 0
                       and all(c in string.hexdigits for c in s))

def xor(s1, s2, type1=10, type2=10):
    """
    XOR 2 strings in base 2 up to base 36.
    Returns decimal int.
    """
    return int(s1, type1) ^ int(s2, type2)

def xorUni(c1, c2):
    """
    XOR 2 unicode characters.
    Return an int.
    """
    return ord(c1) ^ ord(c2)

def hexToUni(s):
    """
    Convert hex string to utf-8.
    """
    raw = bytes.fromhex(s)
    return raw[:-1].decode()

def base64ToUni(s):
    """
    Convert base 64 string to utf-8.
    """
    raw = base64.b64decode(s)
    return raw.decode()

def base64ToHex(s):
    """
    Convert base 64 string to hex string.
    """
    raw = base64.b64decode(s)
    hexStr = base64.b16encode(raw)
    return hexStr.decode()

if __name__ == "__main__":
    test1 = "hello"
    test2 = "00"
    test3 = "686974207468652062756c6c277320657965"
    print(isHex(test1) == False)
    print(isHex(test2) == True)
    print(isHex(test3) == True)
    print(xor("10","10") == 0)
    print(xor("aa","ff",16,16) == 85)
