# -*- coding: utf-8 -*-
# Author: Tiny
# Date  : June 21, 2011
# email : plakitboy@gmail.com

# Lowercase
'''
Description:

Given a string write a program to convert it into lowercase.

Input sample:
The first argument will be a text file containing sentences, one per line. You can assume all characters are from the english language. e.g. 

HELLO CODEEVAL
This is some text

Output sample:
Print to stdout, the lowercase version of the sentence, each on a new line.
e.g.

hello codeeval
this is some text
'''

import sys

if __name__=='__main__':
	file=open(sys.argv[1],'r')
	try:
		for line in file:
			line=line.strip()
			print line.lower()
	finally:
		file.close()
