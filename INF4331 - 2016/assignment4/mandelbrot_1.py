#!/usr/bin/env python3
from numpy import *
import time
import matplotlib.pyplot as plt
import sys

if len(sys.argv) > 1:
    xMin = float(sys.argv[1])
    xMax = float(sys.argv[2])
    yMin = float(sys.argv[3])
    yMax = float(sys.argv[4])
    width = int(sys.argv[5])
    height = int(sys.argv[6])
    numberOfIterations = int(sys.argv[7])
else:
	xMin = -2.25
	xMax = 0.75
	yMin = -1.5
	yMax = 1.5
	width = 1000
	height = 1000
	numberOfIterations = 1000

xValue = linspace(xMin, xMax, width)
yValue = linspace(yMin, yMax, height)

z = complex(0,0)


resultValues = zeros((len(xValue), len(yValue)), int)

t0 = time.clock()

for x in range(len(xValue)):
	for y in range(len(yValue)):
		z=complex(0,0)
		c = complex(xValue[y], yValue[x])
		for iteration in range(numberOfIterations):
			z = (z * z) + c
			if abs(z) > 2:
				resultValues[x][y] = iteration
				break
			else:
				resultValues[x][y] = numberOfIterations

t1 = time.clock()
print('{:.3f} sec'.format(t1 - t0))

plt.figure()
plt.imshow(resultValues, origin='lower', extent=(0, width, 0, height))
plt.savefig("mandelbrot_1.pdf")
plt.show()