import re
import sys
import subprocess

startnow = 0;
class Prepro:
	#metoden __init__(self) kjOrer seg selv nAr klassen blir kalt pA.
	
	def __init__(self):
		latex_fOr = "tex_before.tex"
		latex_etter = "tex_after.tex"
		filinn = open(latex_fOr, 'r')
		#heleTeksten = filinn.read()
		linjerLest = filinn.readlines()
		filut = open(latex_etter, 'w')
		filut.writelines(linjerLest)
		filut.close()
		#self.skrivTilFil(latex_etter, linjerLest)
		filinn.close()

		self.lesfil(latex_etter)

	def tester(testinn):
		if testinn == 0:
			print "ERROR!!!"
			sys.exit(1)

	def skrivTilFil(self, latex_etter, skriveTekst):
		filut = open(latex_etter, 'a')

		filut.write("\\begin{Verbatim}\n")
		#for i in skriveTekst:
		filut.writelines(skriveTekst[0])
		filut.write("\n\end{Verbatim}\n")
		filut.close()

	def skrivTilFil2(self, latex_etter, skriveTekst):
		filut = open(latex_etter, 'a')

		filut.write("\\begin{Verbatim}\n")
		#for i in skriveTekst:
		filut.writelines(skriveTekst)
		filut.write("\n\end{Verbatim}\n")
		filut.close()

	def lesfil(self, latex_etter):
		filinn = open(latex_etter, 'r')
		#heleTeksten = filinn.read()
		linjerLest = filinn.readlines()
		#filut = open(latex_etter, 'w')
		#filut.writelines(linjerLest)
		#filut.close()
		#self.skrivTilFil(latex_etter, linjerLest)
		filinn.close()

		#TESTER
		test_import = 0

		#leser linje for linje
		for linje in linjerLest:
			#deler opp i ord med " ".. ordene er nA en array
			ordene = linje.split(" ")
			for tegn in ordene:
				if tegn == "%@import":
					print ordene[0:]
					tekst = self.oppg1(ordene[1], ordene[2:], latex_etter)
					print tekst
					print "hh"
					self.skrivTilFil(latex_etter, tekst)
					self.erstatt(ordene[0:], tekst)
				if tegn == "%@exec":
					tekst,out,err = self.oppg2(ordene[1:])
					self.skrivTilFil2(latex_etter, "$ " + tekst + "\n" + out[:-1])
				if tegn == "\input":
					self.oppg8(ordene[1], latex_etter)
	def erstatt(self, tekst, svar):
		print "2"
		print str(svar)
		print "3"
		f = open("tex_before.tex", 'r')
		ff = open("tex_after.tmp", 'w')
		for line in f:
			ff.write(line.replace(str(tekst[0:]), str(svar)))

		f.close()
		ff.close()

	def oppg8(self, kjOrefil, latex_etter):
		print "f"

	def oppg2(self, kjOrefil):
		exeStr = ""
		char = ""
		print "RIKTIG EXEC"
		for char in kjOrefil[0:]:
			if char != ' ':
				exeStr += "%s " % (char)
		exeStr = exeStr[:-2]
		for i in exeStr:
			exeStrOrdene = exeStr.split(" ")
		print exeStrOrdene

		proc = subprocess.Popen(exeStrOrdene, stdout=subprocess.PIPE)
		out, err = proc.communicate()
		return (exeStr,out,err)

	def oppg1(self, kjOrefil, regex, latex_etter):
		#linjer = self.lesfil(latex_fil)
		regStr = ""

		print "RIKTIG IMPORT"###################################
		py_fil = open(kjOrefil,'r')
		py_fil_tekst = py_fil.read()
		for char in regex:
			if char != ' ':
				regStr += "%s " % (char)
		regStr = regStr[:-2]
		regStr = re.findall(regStr,py_fil_tekst)
		return regStr

#kjOrer klasses Prepro
x = Prepro()
