import re
import sys
import subprocess

class Prepro:
	#metoden __init__(self) kjOrer seg selv nAr klassen blir kalt pA.
	def __init__(self):
		print "funker"
		self.oppg1og2("tex_before.tex")

	def oppg1og2(self, latex_fil):
		latex_fOr = latex_fil
		latex_etter = "tex_after.tex"

		filinn = open(latex_fOr, 'r')
		filut = open(latex_etter, 'r+')
		linjer = filinn.readlines();

		regStr = ""
		exeStr = ""

		#TESTENE
		test = 0
		test1 = 0

		#leser linje for linje
		for linje in linjer:
			#deler opp i ord med " ".. ordene er nA en array
			ordene = linje.split(" ")
			for ordet in ordene:
				if ordet == "%@import":
					print "RIKTIG"###################################
					py_fil = open(ordene[1],'r')
					py_fil_tekst = py_fil.read()
					test = 1
					for char in ordene[2:]:
						if char != ' ':
							regStr += "%s " % (char)
				if ordet == "%@exec":
					print "RIKTIG 2"
					test1 = 1
					for char in ordene[1:]:
						if char != ' ':
							exeStr += "%s " % (char)



		if test == 0 or test1 == 0:
			print "ERROR - %@import ikke funnet!!!"
			sys.exit(1)

		regStr = regStr[:-2]
		exeStr = exeStr[:-2]


		regStr = re.findall(regStr,py_fil_tekst)

		filut.write("\\begin{Verbatim}\n")
		for i in regStr:
			filut.writelines(i)
		filut.write("\n\end{Verbatim}\n")


		for i in exeStr:
			exeStrOrdene = exeStr.split(" ")
		print exeStrOrdene

		proc = subprocess.Popen(exeStrOrdene, stdout=subprocess.PIPE)
		out, err = proc.communicate()
		if err == "None":
			filut.write("\\begin{Verbatim}\n")
			filut.write("$ ")
			for i in exeStr:
				filut.writelines(i)
			for i in err:
				filut.writelines(i)
			filut.write("\n\end{Verbatim}\n")
		else:
			filut.write("\\begin{Verbatim}\n")
			filut.write("$ ")
			for i in exeStr:
				filut.writelines(i)
			filut.write("\n")
			for i in out:
				filut.writelines(i)
			filut.write("\end{Verbatim}\n")


		filinn.close()
		filut.close()
#kjOrer klasses Prepro
###x = Prepro() funker ogsA
x = Prepro()
#x.__init__()