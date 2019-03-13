from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json


access_token = "chave"
access_token_secret = "chave"
consumer_key = "chave"
consumer_secret = "chave"
tweets_file = open("DATA.json", "a")


class StdOutListener(StreamListener):

    def on_data(self, data):
        print('\x1b[31m')
        print(data)
        tweets_file.write(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track=['keywords'])
