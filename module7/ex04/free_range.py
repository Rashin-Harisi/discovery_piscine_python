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
		arr.append(a)
		while (a != b) :
			a += 1
			arr.append(a)
	print("[", end="")
	for i in range(len(arr)):
		if (i == len(arr)-1):
			print(f"{arr[i]}]")
		else :
			print(f"{arr[i]}, ", end="")
		
