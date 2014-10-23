import subprocess
import os
import re

#Velger hvilken fil som skal pdflatex kompileres
#antatt at "tex_error.tex" er en bestemt -.tex fil kun for dette programmet.
error_latex = "tex_error.tex"

#skriver inn kommandoen som skal kjOres og lagrer resultatet i out.
proc = subprocess.Popen("pdflatex -file-line-error -interaction=nonstopmode " + error_latex, shell=True, stdout=subprocess.PIPE)
out, err = proc.communicate()

print out

#leser -.log filen for A kunne hente de 2 siste linjene i filen
#[:-3] fjerner de 3 siste tegnene ("tex") i stringen error_latex#
#og legger til "log"
#pA denne mAten kan programmet fungere i alle tilfeller,
#dersom antakelsen over hadde heller vAErt et argument fra kommmabdolinje,
#nAr compile.py kjOres
error_log = error_latex[:-3]+"log"

log_fil = open(error_log,'r')
#leser filen linje for linje, linjer = en vektor
linjer = log_fil.readlines();

antall_linjer = len(linjer)
print antall_linjer
#De to siste linjene i alle -.log filer er "\n" og "\n"
#Og antall_linjer er antall linjer i filen MINUS 1,
#fordi linje vektoren starter fra element 0...(f.eks. 98) pA en 99 linjers fil
#Da tar jeg -3 og -2 for A ikke lese "\n+\n" og "\n" og MINUS 1
print linjer[antall_linjer-3] + linjer[antall_linjer-2]

log_fil.close()