# Sum of Intergers form files
'''
Description:
Print out the sum of integers read from a file.
Input sample:
The first argument to the program will be a text file containing a positive integer, one per line. e.g. 
5
12

Output sample:
Print out the sum of all the integers read from the file. 
e.g.
17
'''


# -*- coding: utf-8 -*-
# Author: Tiny
# Date  : July 14, 2011
# email : plakitboy@gmail.com

import sys
if __name__=='__main__':
	result=0
	try:
		file=open(sys.argv[1],'r')
		for line in file:
			result += int(line.strip())
	finally:
		print result


