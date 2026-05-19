#!/usr/bin/env python3

import sys

i = len(sys.argv) - 1

if ( i < 2) : 
	print("none")
else :
	while ( i > 0):
		print(sys.argv[i])
		i = i - 1
