#!/usr/bin/env python3

a = input("Enter the first number : \n")
b = input("Enter the second number : \n")

mult = int(a) * int(b)

print(f"{a} x {b} = {mult}")

if mult > 0 :
	print("The result is positive.\n")
elif mult < 0 :
	print("The result is negative.\n")
else : 
	print("The result is positive and negative.\n")
