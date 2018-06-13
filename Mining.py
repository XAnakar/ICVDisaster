from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

#-------------VARIAVEIS PRO CALCULO--------
access_token = 	"1613384892-spDqJHqobIUfPPSzpYd2EsPM1RoyK9iQfXmf7w1"
access_token_secret = "RaXk2WZnEejaW3jhBAjHIJJyBKzW1JcSNVugMOjEEzukW"
consumer_key = "y6ThN6OR7zNJXIg3a1MFsqoj3"
consumer_secret = "bk80NUmIBmgDNcx128J07eFlvXj4MHbc2AU10sFhh4eyljTWk1"
tweets_file = open("DATA.json", "a")

class StdOutListener(StreamListener):


    def on_data(self, data):
        print('\x1b[31m')
        print(data)
        tweets_file.write(data)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':
    
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track=[ 'amor']) #Aceita até 400 Tags 

