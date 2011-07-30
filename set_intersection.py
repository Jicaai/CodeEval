# -*- coding: utf-8 -*-
# Author: Tiny
# Date  : July 22, 2011
# email : plakitboy@gmail.com

# Set Intersection
'''
Description:

You are given two sorted list of numbers(ascending order). The lists themselves are comma delimited and the two lists are semicolon delimited. Print out the intersection of these two sets.
Input sample:
File containing two lists of ascending order sorted integers, comma delimited, one per line. e.g. 
1,2,3,4;4,5,6
7,8,9;8,9,10,11,12

Output sample:
Print out the ascending order sorted intersection of the two lists, one per line
e.g.
4
8,9
'''

import sys
file = open(sys.argv[1],'r')
try:
	for line in file:
		result = []
		row = line.split(';')
		l1 = row[0].split(',')
		l2 = row[1].split(',')
		for i in xrange(len(l2)):
			if l2[i] in l1:
				result.append(l2[i])
		print ','.join(map(str,result))
finally:
	file.close()


