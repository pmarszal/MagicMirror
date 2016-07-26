from mako.template import Template
import time
import praw
import urllib
import json
import weather
maintemplate = Template(filename='/var/www/templates/home.html')



#Time and Date
t = time.localtime()
hour = t[3]
if len(str(hour)) <2:
	hour = "0"+str(hour)
else:
	hour = str(hour)
minute = t[4]
if len(str(minute)) <2:
	minute = "0"+str(minute)
else:
	minute = str(minute)
date = str(t[2]) +"."+ str(t[1]) +"."+ str(t[0])
wddict = ["Monday", "Tuesday" , "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
weekday =wddict[t[6]]

shower_f=open("/var/www/data/showerthought.json", "r")
showerthought = json.load(shower_f)["showerthought"]

#Weather Today
icon_dict ={"Clear":"/images/sun.svg", "Rain":"/images/rain.svg", "Clouds":"/images/cloud.svg"}

f = open("/var/www/data/proc_data.json","r")
weather_obj = json.load(f)

temperature = weather_obj["temperature"]
temperature_std = weather_obj["temperature_std"]
weather_main = weather_obj["weather_main"]
weather_hour = weather_obj["weather_desc"]

#Render HTML
renderedfile = open('/var/www/html/home.html', 'w')
renderedfile.write(maintemplate.render(
	hour=hour, minute=minute,
	weekday = weekday,
	date=date,
	Message='',
	showerthought = showerthought,
	temp=temperature,
	temp_std = temperature_std,
	wea_desc = weather_hour,
	tdwthicon=icon_dict[weather_main]
	))

renderedfile.close()

