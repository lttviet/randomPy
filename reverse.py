#!/usr/bin/python3

import os
import sys

# Read from end of file buffsize bytes
# Reverse what is read
class BackwardReader:
    def __init__(self, filename, buffsize=4096):
        self.filename = filename
        self.f = open(self.filename, "r")
        self.buffcount = 1
        self.buffsize = buffsize
        self.size = os.stat(self.filename)[6]
        self.data = []

    def read(self):
        start = False       # True when reach the start of file
        while not start:
            try:
                self.f.seek(-self.buffsize*self.buffcount, 2)
                string = self.f.read(self.buffsize)
            except IOError: # reach start of file
                self.f.seek(0)
                s = self.f.read(self.size -
                    self.buffsize*(self.buffcount-1))
                start = True

            self.data.append(s[::-1])
            # remove new line symbol at the end of file
            if self.buffcount == 1 and self.data[0][0] == "\n":
                self.data[0] = self.data[0][1:]
            self.buffcount += 1

        self.f.close()      # close file
        if not self.data:   # empty string
            return ""
        return self.data

if __name__ == "__main__":
    try:
        text = BackwardReader("test.txt")
    except IOError:
        print("Can't open file")
        sys.exit()
    arr = text.read()
    with open("result.txt", "w") as f:
        for s in arr:
            print(s)
            f.write(s)
