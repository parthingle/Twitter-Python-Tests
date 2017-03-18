# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json
import tweepy
import urllib
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys
# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '611030781-0VuUBdJqtq5KLMKYJ1k6UOqXFXblHhmwuGFNdwVZ'
ACCESS_SECRET = 'e1GcCCWKpndCiYvBvzNmgxbCksGb7ktzI1Ne1wdDNZT1n'
CONSUMER_KEY = 'xfg7okUYfazB5t31i9CtRCMkq'
CONSUMER_SECRET = 'qt2ngmhSHDXvAZZBbJK4xc2X6WYHNTduFUWkcVFoY5q5Gxne33'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)


auth = tweepy.OAuthHandler('xfg7okUYfazB5t31i9CtRCMkq', 'qt2ngmhSHDXvAZZBbJK4xc2X6WYHNTduFUWkcVFoY5q5Gxne33')
auth.set_access_token('611030781-0VuUBdJqtq5KLMKYJ1k6UOqXFXblHhmwuGFNdwVZ', 'e1GcCCWKpndCiYvBvzNmgxbCksGb7ktzI1Ne1wdDNZT1n')


# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
iterator = twitter_stream.statuses.sample()

# Print each tweet in the stream to the screen 
# Here we set it to stop after getting 1000 tweets. 
# You don't have to set it to stop, but can continue running 
# the Twitter API to collect data for days or even longer. 
api = tweepy.API(auth)
public_tweets = api.home_timeline()

txts=[]
wr_file = open('ipjson.json', 'a+')
tweet_count = 1

splstring = ""
for tweet in iterator:
    tweet_count -= 1
    # Twitter Python Tool wraps the data returned by Twitter 
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
    #jtxt= json.dumps(tweet)
    splstring+=json.dumps(tweet)
    splstring+='\n'
    if tweet_count <= 0:
        break 
    #jsontxt = json.loads(jsontext)

print (type(splstring))

#print (splstring)
wr_file.write(splstring)
wr_file.flush()

jd = json.loads(splstring)
#json_decode2 = json.dumps(json_decode)
for item in jd:
    textitem = item.get("text")
    txts.append(textitem)



   # print (tweet.text)
    #print("\n\n")
    
    # The command below will do pretty printing for JSON data, try it out
    # print json.dumps(tweet, indent=4)
     
print (txts)