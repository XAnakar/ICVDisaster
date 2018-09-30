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

tweets = api.search('Trump')

for tweet in tweets:
    frase = TextBlob(tweet.text)

    if frase.detect_language() != 'en':
        traducao = TextBlob(str(frase.translate(to='en')))
        print('Tweet: {0} - Sentimento: {1}'.format(tweet.text, traducao.sentiment))
    else:
        print('Tweet: {0} - Sentimento: {1}'.format(tweet.text, frase.sentiment))