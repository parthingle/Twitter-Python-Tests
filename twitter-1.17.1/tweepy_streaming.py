
import tweepy

from tweepy import Stream
from tweepy.streaming import StreamListener

import sys

auth = tweepy.OAuthHandler('xfg7okUYfazB5t31i9CtRCMkq', 'qt2ngmhSHDXvAZZBbJK4xc2X6WYHNTduFUWkcVFoY5q5Gxne33')
auth.set_access_token('611030781-0VuUBdJqtq5KLMKYJ1k6UOqXFXblHhmwuGFNdwVZ', 'e1GcCCWKpndCiYvBvzNmgxbCksGb7ktzI1Ne1wdDNZT1n')

api = tweepy.API(auth)




public_tweets = api.home_timeline()
for tweet in public_tweets:
    print (tweet.text)
    print("\n\n")
    



 