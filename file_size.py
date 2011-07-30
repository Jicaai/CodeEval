# -*- coding: utf-8 -*-
# Author: Tiny
# Date  : July 14, 2011
# email : plakitboy@gmail.com

# File size
'''
Description:
Print the size of a file in bytes.

Input sample:
Path to a filename. e.g. 

foo.txt
Output sample:
Print the size of the file in bytes.
e.g.

55
'''


import os.path
import sys
if __name__=='__main__':
	#filename=raw_input("Enter file name:\n")
	filename=sys.argv[1]
	if os.path.exists(filename):
		print os.path.getsize(filename)
	else:
		print "File does not exist!"
