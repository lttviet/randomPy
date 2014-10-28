#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Give a hex string which has been xor against a single char.
# Find the key and decrypt the message

import sys
import string
import util

def score(text):
    """
    Based on the letter frequency in English, give a text a score.
    """
    freq = {"a": 8, "b": 1, "c": 3, "d": 4, "e": 13, "f": 2, "g": 2, "h": 6,
            "i": 7, "j": 1, "k": 1, "l": 4, "m": 2, "n": 7, "o": 8, "p": 2,
            "q":1, "r": 6, "s": 6, "t": 9, "u": 3, "v": 1, "w": 2, "x": 1,
            "y": 2, "z": 1, " ": 14}
    score = 0
    for letter in text:
        letter = letter.lower()
        if letter in freq:
            score += freq[letter]
        elif letter in string.digits:
            score += 1
        elif letter in string.punctuation:
            score += 0
        elif letter in string.whitespace:
            score -= 1
        else:
            score -= 20
    return score

def decrypt(text, key):
    """
    XOR 1 byte of decrypted text with a single byte key.
    Returns the decrypted text.
    """
    result = ""
    # 1 byte is represented by 2 hex digits
    for b in range(0, len(text), 2):
        result += chr(util.xor(text[b:b+2],key,16,16))
    return result

def attack(text):
    """
    Given a ciphertext, XOR the text against all 256 ascii characters.
    Score each result and return the string with highest score.
    """
    bestScore = 0
    bestText = ""
    bestKey = ""
    for i in range(256):
        key = hex(i)
        temp = decrypt(text, key)
        if score(temp) > bestScore:
            bestText = temp
            bestScore = score(temp)
            bestKey = chr(i)
    return (bestText, bestScore, bestKey)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage:\t{} [path/]filename".format(sys.argv[0]))
        sys.exit()

    try:
        for line in open(sys.argv[1]):
            # remove '\n' at the end of each line
            print(attack(line[:-1]))
    except IOError:
        print("Couldn't open the file {}".format(sys.argv[1]))
