import re
import sys
import string
import subprocess

startnow = 0;
class Prepro:
	#metoden __init__(self) kjOrer seg selv nAr klassen blir kalt pA.
	
	def __init__(self):
		#latex_fOr = "tex_before.tex"
		latex_fOr = "test.tex"
		latex_etter = "tex_after.tex"

		filinn = open(latex_fOr, 'r')
		linjerLest = filinn.readlines()
		filut = open(latex_etter, 'w')
		filut.writelines(linjerLest)
		filut.close()
		filinn.close()

		self.lesfil(latex_etter)

	def skrivTilFil(self, latex_etter, pattern,  skriveTekst):
		filinn = open(latex_etter, 'r')
		tekst = filinn.readlines()
		filinn.close()

		filut = open(latex_etter, 'w')
		filut.writelines(tekst)
		filut.seek(0)
		
		begin = "\\begin{Verbatim}\n"
		end = "\n\end{Verbatim}\n\n"
		skriveTekst = begin + skriveTekst + end
		
		for line in tekst:
			filut.write(line.replace(pattern, skriveTekst[:-1]))		

		filut.close()

	"""
	def skrivTilFil2(self, latex_etter, skriveTekst):
		filut = open(latex_etter, 'a')

		filut.write("\\begin{Verbatim}\n")
		#for i in skriveTekst:
		filut.writelines(skriveTekst)
		filut.write("\n\end{Verbatim}\n")
		filut.close()
	"""
	def lesfil(self, latex_etter):
		filinn = open(latex_etter, 'r')
		linjerLest = filinn.readlines()
		filinn.close()

		#TESTER
		test_import = 0

		#leser linje for linje
		for linje in linjerLest:
			#deler opp i ord med " ".. ordene er nA en array
			ordene = linje.split(" ")
			for tegn in ordene:
				if tegn == "%@import":
					svar = self.oppg1(ordene[1], ordene[2:], latex_etter)
					
					pattern = ""
					for i in ordene[0:]:
						pattern += str(i) + " "
					pattern = pattern[:-1]

					self.skrivTilFil(latex_etter, pattern, svar[:-6])
				if tegn == "%@exec":
					tekst,output= self.oppg2(ordene[1:])

					pattern = ""
					for i in ordene[0:]:
						pattern += str(i) + " "
					pattern = pattern[:-2]

					self.skrivTilFil(latex_etter, pattern, "$ " + tekst[0:] + "\n" + output)
				if tegn == "\input":
					filnavn = ""
					for i in ordene[1:]:
						filnavn += str(i) + " "
						filnavn = filnavn[:-2]
					print filnavn
					
					#self.oppg8(filnavn, latex_etter)

	def oppg8(self, kjOrefil, latex_etter):
		self.lesfil(kjOrefil)

		print "f"

		"""
		global startnow;
		latex_fOr = kjOrefil
		latex_etter = "tex_after.tex"

		linjer = self.lesfil(latex_fil)
		filut = open(latex_etter, 'w')
		input_fil_tekst = ""
		input_fil_tekst_tegn = ""

		test = 0
		test1 = 0
		printalready = 0;
		for linje in linjer:
			printalready = 0;
			#deler opp i ord med " ".. ordene er nA en array
			ordene = linje.split(" ")
			for ordet in ordene:
				if ordet == "\input":
					for char in ordene[1]:
						if char != '\n':
							input_fil_tekst_tegn += "%s" % (char)

					print input_fil_tekst_tegn
					input_fil = open(input_fil_tekst_tegn,'r')
					input_fil_tekst += input_fil.read()

					print input_fil_tekst
					test = 1
					test1 = 1
					if(startnow == 0):
						filut.write("\\begin{Verbatim}\n")
						#for i in input_fil_tekst:
						filut.writelines(input_fil_tekst)
						filut.write("\n\end{Verbatim}\n")
					else:
						filut.writelines(input_fil_tekst)
					printalready = 1;
			if printalready == 0 and startnow == 1:
				filut.writelines(linje);
		"""
	def oppg2(self, kjOrefil):
		exeStr = ""
		char = ""
		for char in kjOrefil[0:]:
			if char != ' ':
				exeStr += "%s " % (char)
		exeStr = exeStr[:-2]
		for i in exeStr:
			exeStrOrdene = exeStr.split(" ")

		proc = subprocess.Popen(exeStrOrdene, stdout=subprocess.PIPE)
		out, err = proc.communicate()
		if (err == None) & (out != None):
			return (exeStr,out[:-1])
		else:
			return (exeStr,err)

	def oppg1(self, kjOrefil, regex, latex_etter):
		regStr = ""

		py_fil = open(kjOrefil,'r')
		py_fil_tekst = py_fil.read()
		for char in regex:
			if char != ' ':
				regStr += "%s " % (char)
		regStr = regStr[:-2]
		regStr = re.findall(regStr,py_fil_tekst)
		

		svartext = ""

		for j in regStr:
			svartext += str(j)
		svartext = svartext[2:-1]
		return svartext

#kjOrer klasses Prepro
x = Prepro()
