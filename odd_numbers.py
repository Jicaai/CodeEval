# -*- coding: utf-8 -*-
# Author: Tiny
# Date  : July 14, 2011
# email : plakitboy@gmail.com

# Odd Numbers
'''
Odd Numbers
Description:
Print the odd numbers from 1 to 99.

Input sample:
None

Output sample:
Print the odd numbers from 1 to 99, one number per line.
'''


def isodd(num):
	return True if num&1 else False

if __name__=='__main__':
	for i in xrange(1,100):
		if isodd(i):
			print i



