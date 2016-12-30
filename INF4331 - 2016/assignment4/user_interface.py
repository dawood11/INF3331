#!/usr/bin/env python
import sys
import subprocess

def help():
	print ("USAGE:\n\tuser_interface.py [xMin] [xMax] [yMin] [yMax] [width] [height] [numberOfIterations] [filename]\n ")

def run(option, xMin, xMax, yMin, yMax, width, height, numberOfIterations):
	if(option) == 1:
		command = "python mandelbrot_1.py", xMin, xMax, yMin, yMax, width, height, numberOfIterations
		cmd = ""
		for x in range(0,len(command)):
			cmd = ' '.join(command)
		process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
		output, error = process.communicate()
	elif(option) == 2:
		command = "python mandelbrot_2.py", xMin, xMax, yMin, yMax, width, height, numberOfIterations
		cmd = ""
		for x in range(0,len(command)):
			cmd = ' '.join(command)
		process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
		output, error = process.communicate()
	elif(option) == 3:
		command = "python mandelbrot_3.py", xMin, xMax, yMin, yMax, width, height, numberOfIterations
		cmd = ""
		for x in range(0,len(command)):
			cmd = ' '.join(command)
		process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
		output, error = process.communicate()
	else:
		print ("ERROR in  run()")

if len(sys.argv) == 1:
	print ("USAGE: --help \n\tuser_interface.py [xMin] [xMax] [yMin] [yMax] [width] [height] [numberOfIterations] [filename]")
elif len(sys.argv) > 1:
	if (sys.argv[1]) == "--help":
		help()
	else:
		xMin = str(sys.argv[1])
		xMax = str(sys.argv[2])
		yMin = str(sys.argv[3])
		yMax = str(sys.argv[4])
		width = str(sys.argv[5])
		height = str(sys.argv[6])
		numberOfIterations = str(sys.argv[7])
		if(sys.argv[8]) == "mandelbrot_1.py":
			run(1, xMin, xMax, yMin, yMax, width, height, numberOfIterations)
		elif(sys.argv[8]) == "mandelbrot_2.py":
			run(2, xMin, xMax, yMin, yMax, width, height, numberOfIterations)
		elif(sys.argv[8]) == "mandelbrot_3.py":
			run(3, xMin, xMax, yMin, yMax, width, height, numberOfIterations)
		else:
			print ("ERROR!!!")