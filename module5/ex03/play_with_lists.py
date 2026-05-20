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

print_arr(numbers)

new_list = []
for i in range(len(numbers)):
	if (numbers[i] > 5) :
		new = numbers[i] + 2
		flag = False
		for j in range(len(new_list)) :
			if (new_list[j] == new) :
				flag = True
				break
		if (flag == False) :
			new_list.append(new)

print_arr(new_list)

#set() => set an array and check for duplication 