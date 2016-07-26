import weather
import json
import praw

x=weather.weather_forecast()
x.download("http://api.openweathermap.org/data/2.5/forecast?lat=51.52&lon=9.93&appid=3b1cc169c1188ce8f299de7a7164d045")

q,w,e,r = x.avge()
dic={"temperature":q, "temperature_std":w, "weather_main":e, "weather_desc":r}

f = open("/var/www/data/proc_data.json", "w")
json.dump(dic,f)
f.close()

#Reddit Showerthought
reddd = praw.Reddit(user_agent="Showerthought-scraper")
showerthought = reddd.get_subreddit("Showerthoughts").get_top_from_day(limit=1).next().title

shower_dic={"showerthought":showerthought}
f=open("/var/www/data/showerthought.json", "w")
json.dump(shower_dic, f)
f.close()


