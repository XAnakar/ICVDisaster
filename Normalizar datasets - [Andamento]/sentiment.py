import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key= 'XLRkRlb7G2seBeo3cvTJPhNCL'
consumer_secret= 'sUQr6Jes8MOMRBXarlrSEclKUjdcvz1XwVuFSawujNfmkzaHcw'

access_token='191826083-UghNS3YwFlUTmnGfyimRBwMmuVdRtRHMCUFfAI7w'
access_token_secret='KyP9MlMpj0MbO3IS1UsdTpEPpBQGMlBGXyX74FqKeWhaL'


auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

name = "jennybrucenyc"
tweetCount = 10
results = api.user_timeline(id=name, count=tweetCount)

for tweet in results:
   print (tweet.geo)

'''
tweets = api.search('Trump')
'''
for tweet in results:
    frase = TextBlob(tweet.text)

    if frase.detect_language() != 'en':
        traducao = TextBlob(str(frase.translate(to='en')))
        print(tweet.text," ->",traducao.sentiment)
    else:
        print(tweet.text," ->",frase.sentiment)