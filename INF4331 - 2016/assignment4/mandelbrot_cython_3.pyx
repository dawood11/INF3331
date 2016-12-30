import cython
import numpy

cdef:
	double xMin = -2.25
	double xMax = 0.75
	double yMin = -1.5
	double yMax = 1.5
	int width = 100
	int height = 100
	int numberOfIterations = 100

	double[:] xValue = numpy.linspace(xMin, xMax, width)
	double[:] yValue = numpy.linspace(yMin, yMax, height)
	int [:,:] resultValues = numpy.empty((width, height), 'int32')

	int i = 0
	int j = 0

	int k
	double zx = 0
	double zy = 0
	double zx2 = 0
	double zy2 = 0

def calculate(xMin, xMax, yMin ,yMax, width, height, numberOfIterations):
	resultValues[:,:] = numberOfIterations
	for i in range(0, width):
		for j in range(0, height):
			x = 0
			y = 0
			xx = 0
			yy = 0
			for k in range(0, numberOfIterations):
				xx = x * x
				yy = y * y
				if(xx + yy > 4.0):
					resultValues[j][i] = k
				y = (x * y * 2) + yValue[j]
				x = xx - yy + xValue[i]
			resultValues[j][i] = numberOfIterations
	return resultValues