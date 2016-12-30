import re
import sys

def diff(string1, string2):
    line1 = string1.split("\n")
    line2 = string2.split("\n")

    matched = ""
    deleted = ""
    added = ""

    output_diff = open("output_diff.txt", 'w')

    for x in line1:
        if re.search(re.escape(x), string2):
            if x != "":
                matched += x + "\n"
                output_diff.writelines("o " + x + "\n")
            else:
                output_diff.writelines("o " + x + "\n")
        else:
            deleted += x + "\n"
            output_diff.writelines("- " + x + "\n")
            for y in line2:
                    if re.search(re.escape(y), string1):
                        if x == "":
                            output_diff.writelines("+ " + y + "\n")
                    else:
                        if re.search(y, added) == None:
                            added += y
                            output_diff.writelines("+ " + y + "\n")
    output_diff.close()


if __name__ == "__main__":
    """
    Making sure the arguments are correct.
    """
    if len(sys.argv) < 3:
        print ("USAGE: \n\t-> pyhton my_diff.py [file1.txt] [file2.txt]\n")
    elif len(sys.argv) > 3:
        print ("USAGE: \n\t-> pyhton my_diff.py [file1.txt] [file2.txt]\n")
    else:
        print("JKDSBF")
        file1 = open(sys.argv[1], 'r')
        file2 = open(sys.argv[2], 'r')

        string1 = file1.read()
        string2 = file2.read()

        diff(string1, string2)
        
        file1.close()
        file2.close()