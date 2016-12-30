- Kjøring/Generelt
Jeg har programmert på min Macbook, som krevde at jeg kjørte filene mine med "python3 rpn.py", alternativt kunne jeg ha "#!/usr/bin/env python3" øverst i fila og kompilert med "chmod a+x rpn.py" og kjøre med "./rpn.py"

på linux maskinene på UiO, fungerer ikke dette optimalt. For å få programmene til å fungere må de kjøres med "/snacks/bin/python3 rpn.py"

- rpn.py
rpn.py fila er kjørbar på 2 måter (uavhengig av hvilken kjøre måte som er valgt over i "Kjøring/Generelt"):
	1. rpn.py "1 2 + p 2.34 4.2 + p -1 * p 20 p 2 / p"
		som bør printe ut:
			-> 3.000
			-> 6.540
			-> -6.540
			-> 20.000
			-> 10.000
		1.1: Negative tall, desimal tall og ikke godkjente tegn og bokstaver har blitt tatt hånd om.
		1.2: For denne type kjøring med argumenter, har jeg valgt å benytte meg av "" ved input, etter som * inkluderte alle filene i mappen.
	2. rpn.py
		>1
		>2
		>+
		...

- wc.py
	1. wc.py helloworld.txt
	2. wc.py *.txt
	3. wc.py *
		- Mapper har blitt tatt hånd om. Det antas at fil format som .pdf ikke befinner seg i mappen OG bokstaver som ikke er gjenkjennelig for tegnsettingen (f.eks.: æ ø å) ikke er inkludert i noen av filene.