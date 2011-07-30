# -*- coding: utf-8 -*-
# Author: Tiny
# Date  : June 11, 2011
# email : plakitboy@gmail.com

# Prime Palindrome
'''
Description:

Write a program to determine the biggest prime palindrome under 1000.
Input sample:
None

Output sample:
Your program should print the largest palindrome on stdout. i.e.
929
'''


def Palindrome(top):
	for i in reversed(xrange(top)):
		if (i==int(str(i)[::-1]))and(isPrime(i)):
			return i
def isPrime(value):
	for i in xrange(2, value):
		if value%i==0:
			return False
		else:
			pass
	return True

if __name__=='__main__':
	print Palindrome(1000)
