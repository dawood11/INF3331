grep -r -l $2 ../$1
if [ $? != 0 ]; then
	echo Dette ordet finnes ikke i noen av filene i filtreet
fi