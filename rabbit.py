#!/usr/bin/python3

import os
import sys

def rabbitNum(time, rate):
    ''' Calculate the number of rabbit pairs after some time periods
        at the reproduction rate.
        Assume 1 young pair at period 1 and rabbits live forever.'''
    assert time >= 1
    assert rate >= 1

    pre, cur = 0, 1
    for i in range(1, time):
        pre, cur = cur, pre * rate + cur
    return cur

def printRabbit(time, rate):
    ''' Output number of rabbits to a format '''
    print("t={:3}\tr={:3}\tnum={}".format(time, rate, rabbitNum(time, rate)))

if __name__ == "__main__":
    printRabbit(1, 100)
    printRabbit(5,3)
    printRabbit(5,1)
    printRabbit(33,2)
