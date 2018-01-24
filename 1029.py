#!/usr/bin/python

str1 = list(input())
str2 = input()

num = 0

for c in str2:
	if c not in str1:
		num = num+1
	else:
		index = str1.index(c)
		str1[index] = '#'
if num == 0:
	print('Yes',str(len(str1)-len(str2)))
else:
	print('No',str(num))
