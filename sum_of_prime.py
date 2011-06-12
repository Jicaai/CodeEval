#Sum of Primes

#Description:
#Write a program to determine the sum of the first 1000 prime numbers.
#Input sample:
#None

#Output sample:
#Your program should print the sum on stdout.i.e.
#3682913

# -*- coding: utf-8 -*-
# Author: Tiny
# Date  : June 11, 2011
# email : plakitboy@gmail.com

def isPrime(value):
	for i in xrange(2, value):
		if value%i==0:
			return False
		else:
			pass
	return True

if __name__=='__main__':
	#for i in xrange(1,1000):
	#	if isPrime(i):
	#		print i
	file=open('isPrime', 'w')
	i=2
	result=0
	count=0
	while(count!=1000):
		if isPrime(i):
			result+=i
			count+=1
		else:
			pass
		i+=1
	print result


