#get top trending tweets
from flask import Flask, render_template
import tweepy #https://github.com/tweepy/tweepy
import random
# import csv

#Twitter API credentials
consumer_key = 'p6IMC2NbVsfepNKLxNiW0MzyU'
consumer_secret = 'UgMLRJ8VCG7RtgKSjdCIQ4RGTkbQHNvj4rMS8xg1CCc12i7CPN'
access_key = '91634289-6YbAoroDNn1mqkkq1lJnGyVfG2DWIFm0l1xRsmFby'
access_secret = 'vnwKLn7vd93BmhUiBQ41Y5aNRbhFUOXtzSbnmXzIpxVFS'


app = Flask(__name__)


@app.route('/trends')

def get_all_trends():
	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	trends_json = api.trends_place(id = "2459115")

	all_trends = []

	all_trends = trends_json[0]['trends'][:10] #getting all 10 trending topics, as individual dictionary objects

	trend_list = [] #probs could do list comprehension, oh well

	#for each dict object, print the name
	for i in all_trends[:10]:
		trend_name = i['name']
		trend_list.append(trend_name)

	random_trend = random.choice(trend_list)
	return random_trend



if __name__ == '__main__':
	#pass in the username of the account you want to download

	# get_all_trends("2459115") #NYC WOEID
	app.run()
