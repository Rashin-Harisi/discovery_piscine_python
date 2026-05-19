#!/usr/bin/env python3

import sys

length = len(sys.argv)

if (length != 2) :
	print("none")
else :
	text = input("What was the parameter? ")
	if (text == sys.argv[1]) : 
		print("Good job!")
	else :
		print("Nope, sorry...")
