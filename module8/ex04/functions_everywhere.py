#!/usr/bin/env python3

import sys

def shrink(text):
    x = slice(8)
    print(text[x])

def enlarge(text):
    length = len(text)
    if (length < 8):
        for i in range(8 - length) :
            text = text + 'Z'
    print(text)

length = len(sys.argv)
if (length == 1):
    print("none")
else :
    for i in range(length -1) :
        if (len(sys.argv[i+1]) > 8) : 
            shrink(sys.argv[i+1])
        elif (len(sys.argv[i+1]) < 8) :
            enlarge(sys.argv[i+1])
        else :
            print(sys.argv[i+1])