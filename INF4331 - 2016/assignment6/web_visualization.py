#!/usr/bin/env python

from flask import Flask, url_for
from flask import render_template
from flask import request
from temperature_CO2_plotter import *
import matplotlib.pyplot as plt

import uuid
import os


app = Flask(__name__)

@app.route("/co2")
def getCO2(error=""):
	co2List = []
	readCo2(co2List)
	return render_template('getCo2.html', co2List=co2List, error=error)

@app.route("/getCo2")
def getTimeCO2(start, end, y_min=-1, y_max=-1, error=""):
	co2List = []

	readCo2(co2List)

	os.system("rm static/*.png")
	name = uuid.uuid4()
	name = "static/" + str(name) + ".png"
	plot_co2(co2List, start, end, y_min, y_max, name)

	return render_template('getCo2.html', co2List=co2List, error=error, name=name)

@app.route("/handle_co2form", methods=['POST'])
def handle_co2form():
	assert request.method == 'POST'

	start_year = request.form["start"]
	end_year = request.form["end"]
	y_min = request.form["min"]
	y_max = request.form["max"]

	if end_year < start_year:
		error="End year can not be earlier than start year!"
		return getCO2(error)
	if y_min == "" or y_max == "":
		y_min = -1
		y_max = -1

	return getTimeCO2(start_year, end_year, y_min, y_max)

@app.route("/temperature")
def getTemperature(error=""):
	temperatureList = []
	readTemperature(temperatureList)
	return render_template('getTemperature.html', temperatureList=temperatureList, error=error)


@app.route("/getTemperature")
def getTimeTemperature(month, start, end, y_min=-100, y_max=-100, error=""):
	temperatureList = []
	readTemperature(temperatureList)

	os.system("rm static/*.png")
	name = uuid.uuid4()
	name = "static/" + str(name) + ".png"

	plot_temperature(temperatureList, month, start, end, y_min, y_max, name)

	return render_template('getTemperature.html', temperatureList=temperatureList, error=error, month=month, name=name)

@app.route("/handle_temperatureform", methods=['POST'])
def handle_temperatureform():
	assert request.method == 'POST'

	month = request.form["month"]
	start_year = request.form["start"]
	end_year = request.form["end"]
	y_min = request.form["min"]
	y_max = request.form["max"]

	if end_year < start_year:
		error="End year can not be earlier than start year!"
		return getTemperature(error)
	if y_min == "" or y_max == "":
		y_min = -100
		y_max = -100
	return getTimeTemperature(month, start_year, end_year, y_min, y_max)

@app.route("/country")
def getCountry(error=""):
	countryList = []
	readCountry(countryList)
	return render_template('getCountry.html', countryList=countryList, error=error)


@app.route("/handle_countryform", methods=['POST'])
def handle_countryform():
	assert request.method == 'POST'

	start_year = request.form["start"]
	end_year = request.form["end"]
	y_min = request.form["min"]
	y_max = request.form["max"]

	if end_year < start_year:
		error="End year can not be earlier than start year!"
		return getCountry(error)
	if y_min == "" or y_max == "":
		y_min = -1
		y_max = -1

	return getTimeCountry(start_year, end_year, y_min, y_max)

@app.route("/getCountry")
def getTimeCountry(start, end, y_min=-1, y_max=-1, error=""):
	countryList = []

	countryList(countryList)

	os.system("rm static/*.png")
	name = uuid.uuid4()
	name = "static/" + str(name) + ".png"

	plot_country(countryList, start, end, y_min, y_max, name)

	return render_template('getCountry.html', countryList=countryList, error=error, name=name)

@app.route("/")
def root():
	return render_template('index.html')

co2List = []
temperatureList = []

if __name__ == '__main__':
	#app.run(host='0.0.0.0', port=1234, debug=True)
	app.run(debug=True)