echo deleting...
find ../$1 -type f -size +$2k
find ../$1 -type f -size +$2k -delete
echo deleted!!!
