#!/bin/bash
find unsorted_fruitskopi | xargs grep ap

echo
echo
echo "$1"
if [ -d ../$1 ] ; then
	echo dette er en mappe
else
	echo dette er shieett
fi