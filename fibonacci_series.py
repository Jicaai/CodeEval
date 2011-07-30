# -*- coding: utf-8 -*-
# Author: Tiny
# Date  : June 21, 2011
# email : plakitboy@gmail.com

# Fibonacci Series
'''
Description:

The Fibonacci series is defined as: F(0) = 0; F(1) = 1; F(n) = F(n-1) + F(n-2) when n>1;. Given a positive integer 'n', print out the F(n).

Input sample:
The first argument will be a text file containing a positive integer, one per line. e.g. 
5
12

Output sample:
Print to stdout, the fibinacci number, F(n).
e.g.
5
144
'''

import sys

def fabonacci(n):
	if n<2:
		return n
	else:
		return fabonacci(n-1)+fabonacci(n-2)

if __name__=='__main__':
	file=open(sys.argv[1],'r')
	try:
		for line in file:
			line=line.strip()
			print fabonacci(int(line))
	finally:
		file.close()
