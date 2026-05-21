#!/usr/bin/env python3

import sys
import re

length = len(sys.argv)
start = 0
i = 0

if (length == 3):
	keyword = sys.argv[1]
	text = sys.argv[2]
	result = re.findall(keyword,text)
	print(len(result))
else :
	print("none")

