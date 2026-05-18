#!/usr/bin/env python3

a = 0
b = 0

while (a < 11):
	print(f"Table of {a}: ", end="")
	b = 0
	while (b < 11):
		print(f"{a * b} ", end="")
		b = b + 1
	print()
	a = a + 1
