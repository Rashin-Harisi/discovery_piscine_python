#!/usr/bin/env python3


numbers = [2, 8, 9, 48, 8, 22, -12, 2]
print("Original list: ",numbers)

new_list = []
for i in range(len(numbers)):
	new_list.append(numbers[i] + 2)

print("New list: ", new_list)

