# -*- coding: utf-8 -*-
# Author: Tiny
# Date  : July 30, 2011
# email : plakitboy@gmail.com

# Bit Positons
'''
Description:
Given a number n and two integers p1,p2 determine if the bits in position p1 and p2 are the same or not. Positions p1,p2 and 1 based.

Input sample:
The first argument will be a text file containing a comma separated list of 3 integers, one list per line. e.g. 
86,2,3
125,1,2

Output sample:
Print to stdout, 'true'(lowercase) if the bits are the same, else 'false'(lowercase).
e.g.
true
false
'''

import sys
file = open(sys.argv[1],'r')
try:
	for line in file:
		row = line.split(',')
		row_int = [int(i) for i in row]
		tested = list(bin(row_int[0]))
		if tested[-row_int[1]]==tested[-row_int[2]]:
			print 'true'
		else:
			print 'false'
finally:
	file.close()
