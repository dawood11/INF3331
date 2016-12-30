printf "\ec"

east=""
west=""
if [ "$2" == "--E" ]; then
	east=true
	echo Eastbound
elif [ "$2" == "--W" ]; then
	west=true
	echo Westbound
elif [ "$#" == 0 ]; then
	echo "$0: No flags! - Default: includes both flags"
else
	echo ""
fi

filename="subway.html"
if [ $# == 0 ] || [ "$1" == "forskningsparken" ] || [ "$1" == "Forskningsparken" ]; then
	echo forskningsparken
	wget -q -O $filename "http://mon.ruter.no/SisMonitor/Refresh?stopid=3010011&computerid=acba4167-b79f-4f8f-98a6-55340b1cddb3&isOnLeftSide=true&blocks=&rows=&test=&stopPoint="


#Linenumber
grep -v ">[0-9]<" $filename > preline.txt
grep "<td class=\"center\">[0-9]" preline.txt | rev | cut -c2 | rev > line.txt

#cut -n -c17- temp.txt > f4.txt

#Destination
grep "td>[ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ]" $filename | cut -c17- > destinationFile.txt

#Time
grep -o "<td>[0-9] \| <td>[0-9][0-9] \| <td>[0-9][0-9]:[0-9][0-9]" $filename | cut -c5- > timee.txt

#Direction
grep -o ">[0-9]<" $filename | cut -c2 > direction.txt

declare -i counter
counter=1
declare -i tmp
> "output.txt"
while [ $counter -lt 10 ]; do
	> "test.txt"
	awk "NR==$counter{print;exit}" line.txt >> "test.txt"
	awk "NR==$counter{print;exit}" destinationFile.txt >> "test.txt"
	echo tid: >> "test.txt"
	awk "NR==$counter{print;exit}" timee.txt >> "test.txt"
	echo retning: >> "test.txt"
	awk "NR==$counter{print;exit}" direction.txt >> "test.txt"
	tr '\n' ' ' < "test.txt"
	tr '\n' ' ' < "test.txt" >> "output.txt"
	echo " " >> "output.txt"
	awk "NR==$counter{print;exit}" output.txt
	tmp=counter+1
	awk "NR==$tmp{print;exit}" output.txt
	((counter++))
done

rm *.txt


elif [ "$1" == "blindern" ] || [ "$1" == "Blindern" ]; then
	echo blindern
	wget -q -O $filename "http://mon.ruter.no/SisMonitor/Refresh?stopid=3010360&computerid=acba4167-b79f-4f8f-98a6-55340b1cddb3&isOnLeftSide=true&blocks=&rows=&test=&stopPoint="


	#Linenumber
	grep -v ">[0-9]<" $filename > preline.txt
	grep "<td class=\"center\">[0-9]" preline.txt | rev | cut -c2 | rev > line.txt

	#cut -n -c17- temp.txt > f4.txt

	#Destination
	grep "td>[ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ]" $filename | cut -c17- > destinationFile.txt

	#Time
	grep -o "<td>[0-9] \| <td>[0-9][0-9] \| <td>[0-9][0-9]:[0-9][0-9]" $filename | cut -c5- > timee.txt

	#Direction
	grep -o ">[0-9]<" $filename | cut -c2 > direction.txt

	declare -i counter
	counter=1
	declare -i tmp
	> "output.txt"
	while [ $counter -lt 10 ]; do
		> "test.txt"
		awk "NR==$counter{print;exit}" line.txt >> "test.txt"
		awk "NR==$counter{print;exit}" destinationFile.txt >> "test.txt"
		echo tid: >> "test.txt"
		awk "NR==$counter{print;exit}" timee.txt >> "test.txt"
		echo retning: >> "test.txt"
		awk "NR==$counter{print;exit}" direction.txt >> "test.txt"
		tr '\n' ' ' < "test.txt"
		tr '\n' ' ' < "test.txt" >> "output.txt"
		echo " " >> "output.txt"
		awk "NR==$counter{print;exit}" output.txt
		tmp=counter+1
		awk "NR==$tmp{print;exit}" output.txt
		((counter++))
	done

	rm *.txt
elif [ "$1" == "nydalen" ] || [ "$1" == "Nydalen" ]; then
	echo nydalen
	curl -s "http://mon.ruter.no/SisMonitor/Refresh?stopid=3012130&computerid=acba4167-b79f-4f8f-98a6-55340b1cddb3&isOnLeftSide=true&blocks=&rows=&test=&stopPoint=" | grep "<td>" -m 18| cut -c17-
	wget -q -O $filename "http://mon.ruter.no/SisMonitor/Refresh?stopid=3010011&computerid=acba4167-b79f-4f8f-98a6-55340b1cddb3&isOnLeftSide=true&blocks=&rows=&test=&stopPoint="
else
	echo "$0: Error!"
fi