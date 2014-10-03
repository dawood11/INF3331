#!/bin/bash

var=0

cd $1

while read -r line; do
var=$((var+1))
done < <(find -type f -size +${2}c)

if (($var==0))
then echo No files of size larger than $2 kilobytes found
else echo Deleting...
	find -type f -size +${2}c | while read -r line; do
	echo $line
	rm $line
	done
fi

echo End of script