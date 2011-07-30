# -*- coding: utf-8 -*-
# Author: Tiny
# Date  : July 30, 2011
# email : plakitboy@gmail.com

# Happy Numbers
'''
Description:

A happy number is defined by the following process. Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers.

Input sample:
The first argument is the pathname to a file which contains test data, one test case per line. Each line contains a positive integer. Each line is in the format: N i.e. a positive integer eg.
1
7
22

Output sample:
If the number is a happy number, print out a 1. If not, print out a 0 eg.
1
1
0
For the curious, here's why 7 is a happy number: 7->49->97->130->10->1. Here's why 22 is NOT a happy number: 22->8->64->52->29->85->89->145->42->18->65->61->37->58->89...

'''
def happy(num):
	line = [int(i) for i in str(num)]
	result = 0
	for x in line:
		result += x**2
	return result



import sys
infile = open(sys.argv[1],'r')
try:
	for line in infile:
		result = 0
		process = []
		line = int(line)
		while True:
			if line!=1:
				if line not in process:
					process.append(line)
					line = happy(line)
				else:
					result =0
					break
			else:
				result = 1
				break
		print result

finally:
	infile.close()
