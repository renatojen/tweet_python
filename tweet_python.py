"""
* 
* TweetEx.py
* Author:
* Renato Jensen Filho
* 2017-01-25
* 
"""

import twitter
from datetime import datetime
from os import getenv
from time import sleep
from random import randrange
#from flask import Flask, render_template, request
#from apscheduler.schedulers.background import BackgroundScheduler
#from apscheduler.triggers.interval import IntervalTrigger

c_key = getenv("TWITTER_CONS_KEY","")
c_secret = getenv("TWITTER_CONS_SCRT","")
a_key = getenv("TWITTER_ACCE_KEY","")
a_secret = getenv("TWITTER_ACCE_SCRT","")
count = 0

twitter_api = twitter.Api(consumer_key=c_key,
                  consumer_secret=c_secret,
                  access_token_key=a_key,
                  access_token_secret=a_secret)

def tweetMe():
	global count
	count = count + 1
	#r = randrange(300)
	dt = str(datetime.now())[:-6].replace(' ', ' - ').replace('.', '') #YYYY-mm-DD - HH:MM:SS
	msg  = dt + " | " +  "It's tweet o' clock! #" +  str(count)
	status = twitter_api.PostUpdate(msg)
	print(status.text)
	"""
	scheduler.add_job(
		func=tweetMe,
		trigger=IntervalTrigger(seconds=(180 + r)),
		id='tweet_job',
		name='Tweeter Service',
		replace_existing	=True)

scheduler = BackgroundScheduler()
scheduler.start	
"""

while True:
	
	tweetMe()
	sleep(180 + randrange(300))
   
"""	   
#
# Flask routines
#

#initializes flask application      
application=Flask(__name__)

@application.route('/')
def index():
   return render_template("index.html", text="")

if __name__=="__main__":
   # Bind to VC_APP PORT/HOST if defined, otherwise default to 5000/localhost.
   PORT = int(getenv('VCAP_APP_PORT', '5000'))
   HOST = str(getenv('VCAP_APP_HOST', 'localhost'))
   application.run(host=HOST, port=PORT)
 """