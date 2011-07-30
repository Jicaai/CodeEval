# -*- coding: utf-8 -*-
# Author: Tiny
# Date  : July 30, 2011
# email : plakitboy@gmail.com

# Rightmost char
'''
Description:

You are given a string 'S' and a character 't'. Print out the position of the rightmost occurrence of 't'(case matters) in 'S' or -1 if there is none. The position to be printed out is zero based.

Input sample:
The first argument is a file, containing a string and a character, comma delimited, one per line. Ignore all empty lines in the input file.e.g. 
Hello World,r
Hello CodeEval,E

Output sample:
Print out the zero based position of the character 't' in string 'S', one per line. Do NOT print out empty lines between your output.
e.g.
8
10
'''

import sys
infile = open(sys.argv[1],'r')
try:
	for line in infile:
		string, character = line.split(',')
		if character.rstrip('\n') not in string:
			print '-1'
		else:
			for i in xrange(len(string)):
				if string[i]== character.rstrip('\n'):
					print i
					break
finally:
	infile.close()
