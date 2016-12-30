#!/usr/bin/env python

import sys
import re
import os
import matplotlib.pyplot as plt
import uuid

def readCo2(List=None):
	"""The function which reads the CO2 to the list.

		Args:
		    param1 (list): With all the items

		Returns:
		    void: Does not return anything
	"""

	co2File = open("assignment6_files/co2.csv", 'r')
	co2Content = co2File.readlines()
	i = 0
	for co2ContentLine in co2Content:
		List.append(co2ContentLine.split(","))
		List[i][1] = List[i][1][:-1]
		i += 1
	co2File.close()
	return List

def printCo2(List=None):
	"""The function which prints the list of CO2

		Args:
		    param1 (list): With all the items

		Returns:
		    void: Does not return anything
	"""

	if List != None:
		for x in range(len(List)):
			print("%s\t%s" % (List[x][0], List[x][1]))
	else:
		print("Nothing to print -> co2")

def plot_co2(List=None, start_year=-1, end_year=-1, y_min=-1, y_max=-1, name=''):
	"""The function which plots the co2.csv from the list

		Args:
			param1 (list): The list containing the data
		    param2 (int): The first/from year
			param3 (int): THe last/to year
			param4 (int): The minimum Y lim
			param5 (int): The maximum Y lim

		Returns:
		    list: retuns the output list
	"""

	if List != None:
		if end_year < start_year:
			print("End year can not be earlier than start year.")
			return

		start = -1
		end = -1

		for x in range(len(List)):
			if List[x][0] == start_year:
				start = x
			if List[x][0] == end_year:
				end = x
		
		if start == -1:
			print("Could not find start date!")
			return
		if end == -1:
			print("Could not find end date!")
			return

		outputList = []
		if y_min == -1 or y_max == -1:
			for x in range(start, end+1):
				#print("%s\t%s" % (List[x][0], List[x][1]))
				outputList.append((List[x][0], List[x][1]))
		else:
			for x in range(start, end+1):
				if float(y_min) <= float(List[x][1]) and float(y_max) >= float(List[x][1]):
					#print("%s\t%s" % (List[x][0], List[x][1]))
					outputList.append((List[x][0], List[x][1]))
		if name != '':
			plot(outputList, 'co2', 'Years', 'Carbon', name)
		else:
			plot(outputList, 'co2', 'Years', 'Carbon')
		return outputList
	else:
		print("Nothing to print -> co2")

def readTemperature(List=None):
	"""The function which reads the temperature to the list.

		Args:
		    param1 (list): With all the items

		Returns:
		    void: Does not return anything
	"""

	temperatureFile = open("assignment6_files/temperature.csv", 'r')
	temperatureContent = temperatureFile.readlines()
	i = 0
	for temperatureContentLine in temperatureContent:
		List.append(temperatureContentLine.split(","))
		List[i][:-1] = List[i][:-1][:-1]
		i += 1
	temperatureFile.close()
	return List

def printTemperature(List=None):
	"""The function which prints the list of Temperatures

		Args:
		    param1 (list): With all the items

		Returns:
		    void: Does not return anything
	"""

	if List != None:
		for x in range(len(List)):
			for y in range(len(List[x])):
				if x > 0:
					if y == 0:
						print("%s" % (List[x][y]), end="\t")
					else:
						print("%0.2f" % (float(List[x][y])), end="\t")
				else:
					print(List[x][y], end="   ")
			print("")
	else:
		print("Nothing to print -> temperature")

def plot_temperature(List=None, month=-1, start_year=-1, end_year=-1, y_min=-100, y_max=-100, name=''):
	"""The function which plots the temperature.csv from the list

		Args:
			param1 (list): The list containing the data
		    param2 (int): The month you'd like to extract
		    param3 (int): The first/from year
			param4 (int): THe last/to year
			param5 (int): The minimum Y lim
			param6 (int): The maximum Y lim

		Returns:
		    list: retuns the output list
	"""

	if List != None:
		if end_year < start_year:
			print("End year can not be earlier than start year.")
			return
		start = -1
		end = -1
		monthNumber = -1
		for x in range(len(List)):
			for y in range(len(List[x])):
				if List[x][y] == month:
					monthNumber = y
					break
			if List[x][0] == start_year:
				start = x
			if List[x][0] == end_year:
				end = x
		
		if monthNumber == -1:
			print("Could not find month!")
			return
		if start == -1:
			print("Could not find start date!")
			return
		if end == -1:
			print("Could not find end date!")
			return
		returnMonth = List[monthNumber]
		outputList = []

		print(List[0][monthNumber])
		if y_min == -100 or y_max == -100:
			for x in range(start, end+1):
				#print("%s" % (List[x][0]), end="\t")
				#print("%0.2f" % (float(List[x][monthNumber])))
				outputList.append((List[x][0], List[x][monthNumber]))
		else:
			for x in range(start, end+1):
				if float(y_min) <= float(List[x][monthNumber]) and float(y_max) >= float(List[x][monthNumber]):
					#print("%s" % (List[x][0]), end="\t")
					#print("%0.2f" % (float(List[x][monthNumber])))
					outputList.append((List[x][0], List[x][monthNumber]))
		"""
		if name != '':
			plot(outputList, 'Temperature: ' + month, 'Years', 'Temperature C°', name)
		else:
			plot(outputList, 'Temperature: ' + month, 'Years', 'Temperature C°')
		"""
		return outputList
	else:
		print("Nothing to print -> temperature")

def plot(Liste=None, title='Plot', xlabel='Time', ylabel='Value', name=''):

	"""The function draws the plot

		Args:
			param1 (list): The list containing the data
		    param2 (string): plot name
		    param3 (string): the label of x-axis
		    param4 (string): the label of y-axis
		    param5 (string): the label name

		Returns:
		    void: the function does not return anything
	"""


	xValues = []
	yValues = []
	for element in Liste:
		xValues.append(element[0])
		yValues.append(element[1])

	plt.clf()
	#plt.close()
	plt.plot(xValues, yValues)

	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.title(title)
	plt.grid(True)
	if name == '':
		name = "static/" + str(uuid.uuid4()) + ".png"
	ax = plt.gca()
	ax.ticklabel_format(useOffset=False)
	plt.savefig(name)

def readCountry(List=None):
	"""The function which reads the country data to the list.

		Args:
		    param1 (list): With all the items

		Returns:
		    void: Does not return anything
	"""

	countryFile = open("assignment6_files/CO2_by_country.csv", 'r')
	countryContent = countryFile.readlines()
	i = 0
	for countryContentLine in countryContent:
		List.append(countryContentLine.split('","'))
		List[i] = List[i]
		List[i][0] = List[i][0][1:]
		List[i][-1] = List[i][-1][:-3]
		i += 1
	List[0][0] = List[0][0][1:]
	#for x in List[1]:
	#	print(x)
	#print(List[1][0])
	countryFile.close()
	return List

def plot_country(List=None, start_year=-1, end_year=-1, y_min=-100, y_max=-100, name=''):

	"""Dedicated function to draw the country plot

		Args:
			param1 (list): The list containing the data
		    param2 (int): The first/from year
			param3 (int): THe last/to year
			param4 (int): The minimum Y lim
			param5 (int): The maximum Y lim
			param6 (string): The name of plot


		Returns:
		    void: the function does not return anything
	"""

	if List != None:
		if end_year < start_year:
			print("End year can not be earlier than start year.")
			return
		start = -1
		end = -1

		for x in range(len(List[0])):
			if List[0][x] == start_year:
				start = x
			if List[0][x] == end_year:
				end = x

		if start == -1:
			print("Could not find start date!")
			return
		if end == -1:
			print("Could not find end date!")
			return

		outputList = []
		
		if y_min == -100 or y_max == -100:
			for x in range(len(List)):
				#print("%s" % (List[x][0]), end="\t")
				#print(List[x][start:end+1])
				#print()
				outputList.append((List[x][0], List[x][start:end+1]))
		if name != '':
			plot(outputList, 'Temperature: ' + month, 'Years', 'Temperature C°', name)
		else:
			plot(outputList, 'Temperature: ' + month, 'Years', 'Temperature C°')
		return outputList
	else:
		print("Nothing to print -> temperature")

if __name__ == "__main__":
	os.system("rm static/*.png")
	
	"""
	co2List = []
	readCo2(co2List)
	plot_co2(co2List, "2007", "2012")
	print("------------------------------------------------")
	plot_co2(co2List, "2007", "2012", "8700", "9510")
	print("************************************************")
	"""

	"""
	temperatureList = []
	readTemperature(temperatureList)
	#temperatureList = readTemperature(temperatureList)
	#printTemperature(temperatureList)
	plot_temperature(temperatureList, "January", "2009", "2012")
	print("------------------------------------------------")
	plot_temperature(temperatureList, "January", "2009", "2012", "-1", "1")
	print("************************************************")
	"""

	countryList = []
	readCountry(countryList)
	print(countryList[0])
	plot_country(countryList, "1960", "1964")
	print("------------------------------------------------")
	#plot_country(countryList, "2009", "2012", "-1", "1")
	print("************************************************")


