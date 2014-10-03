#!/bin/bash
#Assignment 1.3
if [ -z $1 ]||[ -z $2 ]; then # if no arguments the program exits. Eliminates an ugly error occurring. 
	echo "usage: sized_delete path size"
	echo "       Deletes all files over the spesific size [kB]"
	exit 
fi

deleted_files=`find "$1" -type f \! -name ".*" -size +$2k -print -delete` #deleting files bigger than the given input argument and assigning the string of deleted files to the variable, "deleted_files".

if [ "$deleted_files" == "" ]; then # if True, then no files are deleted, since no files where found. 
	echo "No file of size $2 kilobytes or larger found."
else
	echo "Deleting... "
	echo "$deleted_files" #printing out the deleted files
fi
