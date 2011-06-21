# Sum of Digits
'''
Description:
Given a positive integer, find the sum of its constituent digits.

Input sample:
The first argument will be a text file containing positive integers, one per line. e.g. 
23
496

Output sample:
Print to stdout, the sum of the numbers that make up the integer, one per line.
e.g.
5
19
'''
# -*- coding: utf-8 -*-
# Author: Tiny
# Date  : June 21, 2011
# email : plakitboy@gmail.com
import sys

if __name__=='__main__':
	file=open(sys.argv[1],'r')
	try:
		for line in file:
			sum=0
			line=line.strip()
			for i in line:
				sum+=int(i)
			print sum
	finally:
		file.close()
