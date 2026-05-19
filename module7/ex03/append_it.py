#!/usr/bin/env python3

import sys

length = len(sys.argv)
fixed = "ism"

if (length < 2) : 
	print("none")
else : 
	for i in range(length -1) :		
		if (sys.argv[i+1].find(fixed, len(sys.argv[i+1]) - len(fixed)) == -1) :
			print(f"{sys.argv[i+1]+fixed}")

