#!/usr/bin/env python3


numbers = [2, 8, 9, 48, 8, 22, -12, 2]

def	print_arr(arr) :
	print("[" , end="")
	for i in range(len(arr)):
		if ( i == len(arr) - 1):
			print(arr[i], end="")
		else :
			print(f"{arr[i]}, ", end="")
	print("]")


print("Original list: ", end="")
print_arr(numbers)

new_list = []
for i in range(len(numbers)):
	new_list.append(numbers[i] + 2)

print("New list: ", end="")
print_arr(new_list)

