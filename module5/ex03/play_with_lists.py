#!/usr/bin/env python3


numbers = [2, 8, 9, 48, 8, 22, -12, 2]
print(numbers)

new_list = set()
for i in range(len(numbers)):
	if (numbers[i] > 5) :
		new_list.add(numbers[i])
print(new_list)

#set() => set an array and check for duplication 