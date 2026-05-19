#!/usr/bin/env python3


numbers = [2, 8, 9, 48, 8, 22, -12, 2]

print("[", end="")
for i in range(len(numbers)) :
	if (i == len(numbers) - 1) : 
		print(numbers[i], end="")
	else :
		print(f"{numbers[i]}, ", end="")
print("]")
