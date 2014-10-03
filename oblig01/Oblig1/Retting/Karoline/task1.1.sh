#!/bin/bash

cd $1

find -mtime -$2 -type f | xargs ls -l -c --sort=size | awk '{print $5, $9}'

echo end of script