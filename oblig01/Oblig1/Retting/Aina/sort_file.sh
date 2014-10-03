#!/bin/bash
#Assignment 1.4
if [ -z "$1" ] || [ -z "$2" ]; then # if no arguments the program exits
	echo "usage: sort_file file1 file2"
	echo "       Sorts an unsorted file1 to a sorted file2"
	exit 
fi
sort $1 > $2 

