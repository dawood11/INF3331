#!/bin/bash
#Assignment 1.2
if [ -z $2 ]||[ -z $1 ]; then # if its not enough input arguments the program exits. Eliminates an ugly error occurring.
	echo "usage: find_word path word"
	echo "       List files with the given word"
	exit 
fi

files=$(grep -r "$2" $1/*) # saves files found in a variable

if [ "$files" == "" ]; then # If files are empty, no files have been found. 
	echo "No files containing \"$2\" found."
else 
	echo "$files"  #if files are non empty, then prints out filenames.
fi
