#!/usr/bin/env python3
"""
print the single line a b c fn
 - "a" is the number of lines in the file
 - "b" the number of words
 - "c" the number of characters
 - "fn" the filename.
"""
import sys
import os

def lines():
	"""
	Counts the number of lines
	"""
	countWord = context.count("\n")
	print('{0:3d}'.format(countWord), end="\t")

def word():
	"""
	Counts the number of words
	"""
	wordsList = context.split()
	words = len(wordsList)
	print('{0:4d}'.format(words), end="\t")

def characters():
	"""
	Counts the number of characters
	"""
	char = 0
	for characters in context:
		char += 1
	print('{0:5d}'.format(char), end="\t\t")

def process():
	lines()
	word()
	characters()
	print (source)

source = ""
context = ""
if len(sys.argv[1:]) == 0:
	print ("Too few arguments!")
else:
	print ("Lines\tWords\tCharacters\tFilename")
	for source in sys.argv[1:]:
		if os.path.isdir(source) is True:
			print ("wc: %s: read: Is a directory", source)
			continue
		else:
			filename = open(source, 'r')
			context = filename.read()
			process()
			filename.close()
