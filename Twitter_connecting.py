#Tweeting.py
# Tweeting.py is a script to obtain data from tweepy to json.

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s

#consumer key, consumer secret, access token, access secret.
ckey='''Insert your own ckey'''
csecret='''Insert your own csecret'''
atoken='''Insert your own atoken'''
asecret='''Insert your own asecret'''

class listener(StreamListener):

    def on_data(self, data):
        
        
        all_data = json.loads(data)
        tweet = all_data["text"]
        sentiment_value, confidence = s.sentiment(tweet)
        print(tweet)
        print('SentimentValue: ', sentiment_value, 'Confidence: ' ,confidence)

        if confidence*100>=80:
            output = open("twitter-out.txt", "a")
            output.write(sentiment_value)
            output.write('\n')
            output.close()

        return True
    
    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Hong Kong"])
