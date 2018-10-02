import tweepy
from textblob import TextBlob


consumer_key= ''
consumer_secret= ''
access_token=''
access_token_secret=''


auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

name = "Trump"
tweetCount = 10
results = api.user_timeline(id=name, count=tweetCount)

for tweet in results:
   print (tweet.geo)

for tweet in results:
    frase = TextBlob(tweet.text)

    if frase.detect_language() != 'en':
        traducao = TextBlob(str(frase.translate(to='en')))
        print(tweet.text," ->",traducao.sentiment)
    else:
        print(tweet.text," ->",frase.sentiment)