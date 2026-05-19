#!/usr/bin/env python3

text = input()

for char in text :
	if char.isupper() : 
		print(char.lower(), end="")
	elif char.islower() :
		print(char.upper(), end="")
	else : 
		print(char, end="")
print()

