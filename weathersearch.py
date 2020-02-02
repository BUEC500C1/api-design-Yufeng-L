# Copyright 2020 Yufeng Lin yflin@bu.edu
# Virtual environment used in this assignment
import csv
import json
import requests

#Get Coordinates of requested airport
def getLoc(airportcode):
	code = airportcode
	with open("airport-codes.csv") as csv_file:
		data = csv.reader(csv_file)

		for row in data:
			if row[0] == airportcode:
				coordinates = row[11].split(',')
				return [coordinates[0].strip(),coordinates[1].strip()]
			else:
				return "Airportcode Not Found"

#Get weather condition of requested coordinates
def getTemp(latitude,longitude):

	dataUrl = 'https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=49b0f5c0d1b764e0ceea806be36ffa46'.format(latitude, longitude)
	response = requests.get(dataUrl)

	if response.status_code == 200:
		print("Connection OK! Data Returned!")
	else:
		print("Something Happened! Error Code: ",response.status_code)
		print(" ")

	data = response.json()
	temp = data["main"]["temp"]
	min_temp = data["main"]["temp_min"]
	max_temp = data["main"]["temp_max"]
	pressure = data["main"]["pressure"]
	humidity = data["main"]["humidity"]
	description = data["weather"][0]["description"]

	print("Here is the weather condition of your requested airport")
	print("--------------------------------------------------------")
	print("Brief Description of weather:",description)
	print("Range of Temp is from {} to {}".format(min_temp,max_temp))
	print("Humidity is:",humidity)
	print("Pressure is:",pressure)


if __name__ == "__main__":
	# latitude = getLoc("KBOS")[0]
	# longitude = getLoc("KBOS")[1]
    # print(type(getLoc("KBOS")))
	# getTemp(latitude,longitude)
    pass


