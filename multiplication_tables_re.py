# -*- coding: utf-8 -*-
# Author: Tiny
# Date  : July 30, 2011
# email : plakitboy@gmail.com
# Multiplication Tables
'''
Description:

Print out the grade school multiplication table upto 12*12.
Input sample:
None

Output sample:
Print out the table in a matrix like fashion, each number formatted to a width of 4. The first 3 line will look like: 
e.g.
1   2   3   4   5   6   7   8   9  10  11  12
2   4   6   8  10  12  14  16  18  20  22  24
3   6   9  12  15  18  21  24  27  30  33  36
'''

for i in xrange(1,13):
	for j in xrange(1,13):
		if j==1:
			print i*j,
		else:
			print str(i*j).rjust(3,' '),
	print '\n',
	


