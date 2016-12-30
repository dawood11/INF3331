#!/usr/bin/env python3
from numpy import *
import matplotlib.pyplot as plt
import time
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


t0 = time.clock()
x, y = meshgrid(linspace(xMin, xMax, width), linspace(yMin, yMax, height))

cValue= x + y*1j

resultValues = zeros((width, height), int)
resultValues[:] = numberOfIterations

zValue = zeros((width, height),'complex64')

for iterations in range(numberOfIterations):
    mask = (resultValues == numberOfIterations)
    zValue[mask] = zValue[mask]**2 + cValue[mask]
    resultValues[mask & (abs(zValue) > 2)] = iterations

t1 = time.clock()
print(t1-t0)
plt.figure()
plt.imshow(resultValues, origin='lower', extent=(0, width, 0, height))
plt.savefig("mandelbrot_2.pdf")
plt.show()
