#!/usr/bin/env python3

import sys

length = len(sys.argv)
flag = False

if (length != 2) :
	print("none")
else :
	text = sys.argv[1]
	for char in text :
		if (char == "z"):
			print("z", end="")
			flag = True
	if (flag == False) :
		print("none")
