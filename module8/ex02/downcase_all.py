#!/usr/bin/env python3

import sys

def downcase_it(str) :
    print(str.lower())

length = len(sys.argv)
if (length == 1) :
    print("none")
else :
    for i in range(length -1) :
        downcase_it(sys.argv[i+1])