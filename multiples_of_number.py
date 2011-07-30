# -*- coding: utf-8 -*-
# Author: Tiny
# Date  : July 30, 2011
# email : plakitboy@gmail.com

# Multiples of a number
'''
Description:

Given numbers x and n, where n is a power of 2, print out the smallest multiple of n which is greater than or equal to x. Do not use division or modulo operator.

Input sample:
The first argument will be a text file containing a comma separated list of two integers, one list per line. e.g. 
13,8
17,16

Output sample:
Print to stdout, the smallest multiple of n which is greater than or equal to x, one per line.
e.g.
16
32
'''
import sys

file =  open(sys.argv[1],'r')
try:
	for line in file:
		threshold, num = map(int, line.split(','))
		tester = 1
		while True:
			if threshold<=num*tester:
				print num*tester
				break
			else:
				tester += 1
finally:
	file.close()
