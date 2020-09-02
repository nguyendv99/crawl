import json
import csv
import tweepy
import re

consumer_key = 'OCfCwmv3FroihdCa5242JkUO7'
consumer_secret = 'hPgCKNl2J5BjrUxkCaCFqIjmFlE63iT3dhe1oTjHeVb97vDojx'
access_token = '222342647-D7chKQaPFtGB51U775EWPfQtN4Gt9TRafGUaaRST'
access_secret = 'q2X36IL9LR988RzcQ7aiWQrDmFpeGImvSjZmpMACwMIYJ'

tweetsPerQry = 100
maxTweets = 1000000
hashtag = "#vietnam"

maxId = -1
tweetCount = 0

authentication = tweepy.OAuthHandler(consumer_key, consumer_secret)
authentication.set_access_token(access_token, access_secret)
api = tweepy.API(authentication, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

with open('data.csv', 'w', encoding="utf-8") as file:
	w = csv.writer(file)
	w.writerow(['idtweet', 'full_text'])
	while tweetCount < maxTweets:
		if(maxId <= 0):
			newTweets = api.search(q=hashtag, count=tweetsPerQry, result_type="recent", tweet_mode="extended")
		else:
			newTweets = api.search(q=hashtag, count=tweetsPerQry, max_id=str(maxId - 1), result_type="recent", tweet_mode="extended")

		if not newTweets:
			print("End")
			break
		
		for tweet in newTweets:
			w.writerow([tweet.id_str, tweet.full_text.replace('\n',' ').encode('utf-8')])

		tweetCount += len(newTweets)	
		maxId = newTweets[-1].id

	
