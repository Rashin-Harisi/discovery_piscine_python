#!/usr/bin/env python3

import sys

params = len(sys.argv)

if (params == 1):
	print("none")
else :
	print(f"parameters: {params-1}") 
	for i in range(params - 1):
		print(f"{sys.argv[i+1]}: {len(sys.argv[i+1])}")
	
