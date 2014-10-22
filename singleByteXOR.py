#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Give a hex string which has been xor against a single char.
# Find the key and decrypt the message

import sys
import string

def score(text):
    """
    Based on the letter frequency in English, give a text a score.
    """
    freq = {"a": 8, "e": 13, "i": 7, "o": 8, "u": 3, " ": 14}
    score = 0
    for letter in text:
        if letter in freq:
            score += freq[letter]
    return score

def decrypt(text, key):
    """
    XOR the decrypted text with a single byte key.
    Returns the decrypted text.
    """
    xor = lambda x, y : int(x,16) ^ int(y, 16)
    result = ""
    # 1 byte is represented by 2 hex digits
    for b in range(0, len(text)-2, 2):
        result += chr(xor(text[b:b+2], key))
    return result

def attack(text):
    """
    Given a ciphertext, XOR the text against all 256 ascii characters.
    Score each result and return the string with highest score.
    """
    bestScore = 0
    bestText = ""
    for i in range(256):
        key = hex(i)
        temp = decrypt(text, key)
        if score(temp) > bestScore:
            bestText = temp
            bestScore = score(temp)
    return (bestText, bestScore)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage:\t{} [path/]filename".format(sys.argv[0]))
    if len(sys.argv) == 2:
        try:
            for text in open(sys.argv[1]):
                print(attack(text))
        except IOError:
            print("Couldn't open the file {}".format(sys.argv[1]))
