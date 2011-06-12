#Reverse words

#Description:
#Write a program to reverse the words of an input sentence.
#Input sample:

#The first argument will be a text file containing multiple sentences, one per line. Possibly empty lines too. e.g. 
#Hello World
#Hello CodeEval

#Output sample:
#Print to stdout, each line with its words reversed, one per line. Empty lines in the input should be ignored. Ensure that there are no trailing empty spaces on each line you print. 
#e.g.
#World Hello
#CodeEval Hello

# Author: Tiny
# Date  : June 12, 2011
# email : plakitboy@gmail.com
import sys


if __name__=='__main__':
	file=open(sys.argv[1],'r')
	try:
		for line in file:
			line=' '.join(line.split()[::-1])
			print line
	finally:
		file.close()
