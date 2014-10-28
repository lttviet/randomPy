#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Given a file in base64 which has been encrypted with repeating-key XOR
# Decrypt it.

import sys
import itertools
import string
import util
import repeatingKeyXOR
import singleByteXOR

def decrypt(text, key):
    """
    XOR the decrypted text in UTF-8 with a single byte key.
    Returns the decrypted text.
    """
    result = ""
    for char in text:
        result += chr(util.xorUni(char, key))
    return result

def attack(text):
    """
    Given a ciphertext in utf-8, XOR the text against all 256 ascii characters.
    Score each result and return the best text, and key.
    """
    bestScore = 0
    bestText = ""
    bestKey = ""
    for i in range(256):
        key = chr(i)
        temp = decrypt(text, key)
        if singleByteXOR.score(temp) > bestScore:
            bestText = temp
            bestScore = singleByteXOR.score(temp)
            bestKey = key
    return (bestText, bestKey)

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
        # normalised average edit distance
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
    keysize = findKeySize(cipher,20)
    key = ""
    blk = divide(cipher, keysize)
    for text in blk:
        (bestText, bestKey) = attack(text)
        key += bestKey
    return key

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage:\t{} [path/]filename".format(sys.argv[0]))

    try:
        with open(sys.argv[1]) as f:
            # convert base64 to utf-8
            cipher = util.base64ToUni(f.read())
            key = findKey(cipher)
            print("Key is: {}".format(key))
            decrypted = repeatingKeyXOR.encrypt(cipher, key)
            print(util.hexToUni(decrypted))
    except IOError:
        print("Couldn't open the file {}".format(sys.argv[1]))
