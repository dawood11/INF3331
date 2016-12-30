#!/usr/bin/env python3
from numpy import *
import matplotlib.pyplot as plt
import matplotlib as mpl
import time
import sys

xMin = -2.25
xMax = 0.75
yMin = -1.5
yMax = 1.5
width = 1000
height = 1000
numberOfIterations = 1000


t0 = time.clock()

xValue = linspace(xMin, xMax, width)
yValue = linspace(yMin, yMax, height)
x, y = meshgrid(xValue, yValue)

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

if (sys.argv[1] == "Orrd"):
    cmap = mpl.cm.OrRd
    plt.imshow(resultValues, cmap = cmap, extent = (min(xValue), max(xValue), min(yValue), max(yValue)))
elif sys.argv[1] == "Flag":
    cmap = mpl.cm.flag
    plt.imshow(resultValues, cmap = cmap, extent = (min(xValue), max(xValue), min(yValue), max(yValue)))
elif sys.argv[1] == "Spring":
    cmap = mpl.cm.spring
    plt.imshow(resultValues, cmap = cmap, extent = (min(xValue), max(xValue), min(yValue), max(yValue)))
else:
    print ("USAGE: mandelbrot_7.py 'Orrd' or 'Flag' or 'Spring'")
    print ("\t-> Default color...")
    plt.imshow(resultValues)

plt.savefig("mandelbrot_7.pdf")
plt.show()
