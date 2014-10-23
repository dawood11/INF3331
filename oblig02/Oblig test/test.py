"""
import re
text = "apple, apples, pineapple and appletini"
print re.findall(r"\w+", text)

print re.sub(r"apple\b", "pear", text) 
print re.findall(r"\apple(\w*)", text) 
print re.sub(r"apple\b(\w*)", "F", text)
#\b etter strenger vil si, alt som har den strenger pA slutten av sin regStr
#\b pA starten av en streng vil si den strenger som starter pA den oppgitte strengern
#resten vil si alt som inneholder den strengen.

#\b = mellomrom
"""
