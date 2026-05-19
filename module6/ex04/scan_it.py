#!/usr/bin/env python3

import sys

length = len(sys.argv)
start = 0
i = 0

if (length == 3):
	keyword = sys.argv[1]
	text = sys.argv[2]
	while True:
		check = text.find(keyword,start)	
		if (check != -1) :
			start =  check + 1
			i += 1
		else : 
			break
	if i == 0 :
		print("none")
	else :
		print(i)
else :
	print("none")

#you can do this exercise with the re.findall(pattern,string)
