#!/usr/bin/env python3

import sys

length = len(sys.argv)
arr = []

if length != 3 :
	print("none")
else:
	a = int(sys.argv[1])
	b = int(sys.argv[2])
	if (a > b) :
		print("The fisrt number should be smaller than the second number")
		sys.exit()
	else : 
		x =list(range(a,b+1,1))
		print(x)
		
