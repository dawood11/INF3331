if [ "$1" == "S" ]; then
	shift;
	declare -i sum; sum=0
	for digit in $@; do
		sum=$(expr $sum + $digit)
	done
	echo $sum
elif [ "$1" == "P" ]; then
	shift;
	declare -i sum; sum=1
	for digit in $@; do
		sum=$(expr $sum \* $digit)
	done
	echo $sum
elif [ "$1" == "M" ]; then
	shift;
	declare -i max; max=$1
	while [ $# -gt 0 ]
	do
		if [ $1 -gt $max ]; then
			max=$1
		fi
		shift;
	done
	echo $max
elif [ "$1" == "m" ]; then
	shift;
	declare -i min; min=$1
	while [ $# -gt 0 ]
	do
		if [ $1 -lt $min ]; then
			min=$1
		fi
		shift;
	done
	echo $min
else
	echo "$0: Invalid option!"
	echo " -> S for sum"
	echo " -> P for product"
	echo " -> M for maximum"
	echo " -> m for minimum "
fi