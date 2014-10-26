#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Given a file in base64 which has been encrypted with repeating-key XOR
# Decrypt it.

import sys
import base64
import itertools
import string
import repeatingKeyXOR

def score(text):
    """
    Based on the letter frequency in English, give a text a score.
    """
    freq = {"a": 8, "b": 1, "c": 3, "d": 4, "e": 13, "f": 2, "g": 2, "h": 6,
            "i": 7, "l": 4, "m": 2, "n": 7, "o": 8, "p": 2, "r": 6, "s": 6,
            "t": 9, "u": 3, "v": 1, "w": 2, "y": 2, " ": 14}
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
            score -= 10
    return score

def decrypt(text, key):
    """
    XOR the decrypted text in UTF-8 with a single byte key.
    Returns the decrypted text.
    """
    xor = lambda x, y: x ^ y
    result = ""
    for char in text:
        result += chr(xor(ord(char), key))
    return result

def attack(text):
    """
    Given a ciphertext in utf-8, XOR the text against all 256 ascii characters.
    Score each result and return the best text, score and key.
    """
    bestScore = 0
    bestText = ""
    bestKey = ""
    for key in range(256):
        temp = decrypt(text, key)
        if score(temp) > bestScore:
            bestText = temp
            bestScore = score(temp)
            bestKey = chr(key)
    return (bestText, bestScore, bestKey)

def distance(s1, s2):
    """
    Find the number of differing bits between 2 equal-length strings.
    XOR 2 strings, the number of 1s in resulting binary number is the answer.
    """
    assert len(s1) == len(s2)
    return sum(bin(ord(c1) ^ ord(c2)).count("1") for (c1, c2) in zip(s1, s2))

def average(blk):
    """
    Given a list of strings, find the average edit distance between them.
    """
    total = 0
    num = 0
    for (s1, s2) in itertools.combinations(blk, 2):
        total += distance(s1, s2)
        num += 1
    return total/num

def findKeySize(cipher, block=4):
    """
    Returns keysize with smallest average edit distance of n block.
    Default is to use average of 4 blocks.
    """
    temp = [0,0]
    for keysize in range(2, 41):
        blk = []
        for i in range(block):
            blk.append(cipher[i*keysize:(i+1)*keysize])
        temp.append(average(blk)/keysize)
    return temp.index(min(temp[2:]))

def divide(cipher, keysize):
    """
    Divide the cipher into blocks of keysize length.
    Returns a list in which the first element contains the first byte of
    every block, the second element the second byte of every block and so on.
    """
    blk = [""]*keysize
    for i in range(0, len(cipher), keysize):
        text = cipher[i:i+keysize]
        for j in range(0,len(text)):
            blk[j] += text[j:j+1]
    return blk

def findKey(cipher):
    """
    Single-byte XOR each element of list, find the character with best score.
    Put them together to get the key.
    """
    #keysize = findKeySize(cipher)
    keysize = findKeySize(cipher, block=20)
    key = ""
    blk = divide(cipher, keysize)
    for text in blk:
        (bestText, bestScore, bestKey) = attack(text)
        key += bestKey
    return key

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage:\t{} [path/]filename".format(sys.argv[0]))
    if len(sys.argv) == 2:
        try:
            with open(sys.argv[1]) as f:
                # convert base64 to utf-8
                cipher = base64.b64decode(f.read())
                cipher = cipher.decode()
                key= findKey(cipher)
                print(key)
                charKey = itertools.cycle(key)
                xor = lambda x,y: chr(ord(x) ^ ord(y))
                for char in cipher:
                    print(xor(char, next(charKey)), end="")
        except IOError:
            print("Couldn't open the file {}".format(sys.argv[1]))
