# -*- coding: utf-8 -*-
# Author: Tiny
# Date  : July 30, 2011
# email : plakitboy@gmail.com

# Self Describing Numbers
'''
Description:

A number is a self-describing number when (assuming digit positions are labeled 0 to N-1), the digit in each position is equal to the number of times that that digit appears in the number.

Input sample:
The first argument is the pathname to a file which contains test data, one test case per line. Each line contains a positive integer. Each line is in the format: N i.e. a positive integer eg.
2020
22
1210

Output sample:
If the number is a self-describing number, print out a 1. If not, print out a 0 eg.
1
0
1
For the curious, here's how 2020 is a self-describing number: Position '0' has value 2 and there is two 0 in the number. Position '1' has value 0 because there are not 1's in the number. Position '2' has value 2 and there is two 2. And the position '3' has value 0 and there are zero 3's.
'''

def sum_of_char(letter,l):
	result = 0
	for x in xrange(len(l)):
		if l[x]== letter:
			result += 1
	return result

def is_describing(num):
	line = [int(i) for i in str(num)]
	dic = dict(enumerate(line))
	result = 1
	for i in dic:
		if sum_of_char(i,line)!=dic[i]:
			result = 0
			break
	return result

import sys

if __name__=='__main__':
	infile =  open(sys.argv[1],'r')
	try:
		for line in infile:
			print is_describing(int(line))
	finally:
		infile.close()



