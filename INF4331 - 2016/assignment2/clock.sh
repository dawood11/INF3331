while true
do
	if [ "$1" == "--AMPM" ]; then
		printf "\ec"
		echo $(date  +"%r")
		sleep 1
	elif [ $# -eq 0 ]; then
		printf "\033c"
		echo $(date  +"%T")
		sleep 1
	else
		echo "$0: $1 is unrecognizeable! "
		exit
	fi
done