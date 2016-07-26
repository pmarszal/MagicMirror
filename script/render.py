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


#Reddit Showerthought
reddd = praw.Reddit(user_agent="Showerthought-scraper")
showerthought = reddd.get_subreddit("Showerthoughts").get_top_from_day(limit=1).next().title

#Weather Today
icon_dict ={"Clear":"/images/sun.svg", "Rain":"/images/rain.svg", "Clouds":"/images/cloud.svg"}

weather_obj = weather.weather_forecast()
weather_obj.download()
temperature, temperature_std, weather_main, weather_hour = weather_obj.avge()

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

