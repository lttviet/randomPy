#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from Crypto.Cipher import AES
import base64

class ECB:
    def __init__(self, key):
        self.key = key.encode()
        self.ECBCipher = AES.new(key, AES.MODE_ECB)

    def encrypt(self, text):
        """
        Encrypt a plain text (byte string) using AES in EBC mode.
        """
        return self.ECBCipher.encrypt(text)

    def decrypt(self, ciphertext):
        """
        Decrypt a ciphertext (byte string) which has been encrypted using AES in EBC.
        """
        return self.ECBCipher.decrypt(ciphertext)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage:\t{} [path/]filename".format(sys.argv[0]))
        sys.exit()

    try:
        KEY = "YELLOW SUBMARINE"
        cipher = ECB(KEY)
        with open(sys.argv[1]) as f:
            ciphertext = base64.b64decode(f.read())
            print(cipher.decrypt(ciphertext))

    except IOError:
        print("Couldn't open the file {}".format(sys.argv[1]))
