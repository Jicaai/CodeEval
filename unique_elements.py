# -*- coding: utf-8 -*-
# Author: Tiny
# Date  : July 30, 2011
# email : plakitboy@gmail.com

# Unique Elements
'''
Description:

You are given a sorted list of numbers with duplicates. Print out the sorted list with duplicates removed.

Input sample:
File containing a list of sorted integers, comma delimited, one per line. e.g.
1,1,1,2,2,3,3,4,4
2,3,4,5,5

Output sample:
Print out the sorted list with duplicates removed, one per line
e.g.
1,2,3,4
2,3,4,5
'''

import sys
infile = open(sys.argv[1],'r')
try:
	for line in infile:
		row = set([int(i) for i in line.split(',')])
		result = list(row)
		result.sort()
		result=[str(i) for i in result]
		print ','.join(result)
finally:
	infile.close()
