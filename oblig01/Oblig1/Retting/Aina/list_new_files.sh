#!/bin/bash
#assignment 1.1
if [ -z $1 ]||[ -z $2 ]; then # if no arguments the program exits. Eliminates an ugly error occurring. 
	echo "usage: list_new_files path days"
	echo "       List files modified in the last n days"
	exit 
fi

find "$1" -type f -mtime -$2 \! -name ".*" | xargs ls -sSr1k  #finding files in the path "$1", last modified $2 days ago

