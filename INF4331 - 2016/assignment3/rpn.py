#!/usr/bin/env python3
"""
The program works with " " as the input.
For example:
 -> 'python rpn.py "1 2 3 + p 1 2 * p 3 + 4 + p"'
 -> 'python3 rpn.py "1 2 3 + p 1 2 * p 3 + 4 + p"'
which should print out 
'5.0'
'2.0'
'9.0'
"""

import math
import signal
import sys

def signal_handler(signal, frame):
	"""
	Handling Ctrl + C signal,
	to quit the program from endless loop
	"""
	print ("You pressed Ctrl+C!")
	sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

stack = []
flag = False
flag2 = False
while True:
	if len(sys.argv) == 2:
		if flag is True:
			sys.exit(0)
		inputValue = sys.argv[1]
		flag = True
	else:
		if flag2 is False:
			print ("Press Ctrl+C to quit!")
		flag2 = True
		inputValue = input("> ")

	inputStack = inputValue.split()
	for value in inputStack:
		if value == '+' or value == '*' or value == '/':
			if len(stack) == 0:
				print ("No values has been entered. Nothing to calculate")
			elif len(stack) == 1:
				print ("Value: ", stack[0], "has nothing to be calculated with")
			else:
				if value == '+':
					stack[-2] = stack[-1] + stack[-2] #replacing 2nd last element from stack
					del stack[-1] #pop last element from stack
				elif value == '*':
					stack[-2] = stack[-1] * stack[-2] #replacing 2nd last element from stack
					del stack[-1] #pop last element from stack
				elif value == '/':
					stack[-2] = stack[-2] / stack[-1] #replacing 2nd last element from stack
					del stack[-1] #pop last element from stack
		elif value == 'v' or value == 'V':
			if len(stack) == 0:
				print ("No values has been entered. Nothing to calculate")
			else:
				stack[-1] = math.sqrt(stack[-1])
		elif value == 'cos' or value == 'COS':
			if len(stack) == 0:
				print ("No values has been entered. Nothing to calculate")
			else:
				stack[-1] = math.cos(stack[-1])
		elif value == 'sin' or value == 'SIN':
			if len(stack) == 0:
				print ("No values has been entered. Nothing to calculate")
			else:
				stack[-1] = math.sin(stack[-1])
		elif value == 'p' or value == 'P':
			if len(stack) == 0:
				print ("There is nothing to be printed out.")
				continue
			#print (stack[-1])
			print("%.3f" % stack[-1])
		#elif value.isdigit() is True or float(value) < 0:
			#stack.append(float(value)) #casting to float, to handle / properly
		else:
			try: #Checking if input is a number at all, including floats
				float(value)
				stack.append(float(value)) #casting to float, to handle / properly
			except ValueError:
				print ("'%s' Is an invalid input." % value)
