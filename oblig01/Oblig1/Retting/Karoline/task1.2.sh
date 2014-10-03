#!/bin/bash

cd $1

var=0

while read -r line; do
var=$((var+1))
done < <(grep -r -n -i $2)

grep -r -n -i $2

if (($var > 0))
then echo Found $var files containing word $2
else echo Found no files containing word $2
fi

echo end of script