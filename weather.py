import urllib
import json
import numpy as np
import time

class weather_forecast():
	icon_dict ={"Clear":"/images/sun.svg", "Rain":"/images/rain.svg", "Clouds"    :"/images/cloud.svg"}
	api_key = "3b1cc169c1188ce8f299de7a7164d045"
	d = {}
	
	considered_range=4	


	def __init__(self):
		return None
	
	def download(self):
		#uu = urllib.urlopen("http://api.openweathermap.org/data/2.5/forecast?lat=5    1.52&lon=9.93&appid=3b1cc169c1188ce8f299de7a7164d045")
		uu = open("weather_data.json", "r")
		self.d = json.load(uu)
	
		#wea = d["list"][0]["weather"][0]["main"]
		#wea_desc = d["list"][0]["weather"][0]["description"]
		#temp = float(d["list"][0]["main"]["temp"])-273.
		
	def avge(self):
		temperature_list = []
		weather_description_list =[]
		weather_class_list=[]
		time_list=[]
		for hourly_forecast in self.d["list"]:
			time_list.append(time.gmtime(hourly_forecast["dt"]))
			temperature_list.append(float(hourly_forecast["main"]["temp"])-273.15)
			weather_class_list.append(hourly_forecast["weather"][0]["main"])
			weather_description_list.append(hourly_forecast["weather"][0]["description"])
			
		temperature_list = np.array(temperature_list)
		
		expected_temperature = temperature_list[:self.considered_range].mean()	
		expected_temperature_std = temperature_list[:self.considered_range].std()
		expected_temperature = str(np.round(expected_temperature, 1))+"("+str(np.round(expected_temperature_std, 1))+")"
		

		weather_counts=[]
		for x in set(weather_class_list[:self.considered_range]):
			counted = [x, weather_class_list[:self.considered_range].count(x)]
			weather_counts.append(counted)
		weather_counts = np.array(weather_counts)
		arg_max_weather = weather_counts[:,1].astype(int).argmax()	
		most_weather = weather_counts[arg_max_weather,0]
		
		hourly_weather = weather_description_list[0]
		
		
		return expected_temperature, most_weather, hourly_weather
