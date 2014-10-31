import re
import sys
import subprocess

startnow = 0;
class Prepro:
	#metoden __init__(self) kjOrer seg selv nAr klassen blir kalt pA.
	
	def __init__(self):
		global startnow;
		latex_fil = "test.tex"

		self.oppg8Input(latex_fil)
		self.oppg1og2(latex_fil)
		while(1==1):	
			startnow = 1;
			latex_fil = "tex_after.tex"
			filetmp4 = open("tmp.tex", 'w');
			filetmp4.write(self.lesfil2(latex_fil))
			filetmp4.close();
			latex_fil = "tmp.tex";
			match = re.search("\input", self.lesfil2("tmp.tex"), flags=0)
			if match:
				self.oppg8Input(latex_fil)
				#break;
				#self.oppg1og2(latex_fil)
				break;
			else:
				break;



	def lesfil(self, latex_fil):
		latex_fOr = latex_fil

		filinn = open(latex_fOr, 'r')
		linjerLest = filinn.readlines()
		filinn.close()

		return linjerLest
	def lesfil2(self, latex_fil):
		latex_fOr = latex_fil

		filinn = open(latex_fOr, 'r')
		linjerLest = filinn.read();
		filinn.close()

		return linjerLest
	##def skrivTilFil(self, latex_fil, latex_etter):
		
	def oppg8Input(self, latex_fil):
		global startnow;
		latex_fOr = latex_fil
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
		

	def oppg1og2(self, latex_fil):
		latex_fOr = latex_fil
		latex_etter = "tex_after.tex"

		filut = open(latex_etter, 'a')
		linjer = self.lesfil(latex_fil)

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


		#filinn.close()
		filut.close()
#kjOrer klasses Prepro
###x = Prepro() funker ogsA
x = Prepro()
#x.__init__()