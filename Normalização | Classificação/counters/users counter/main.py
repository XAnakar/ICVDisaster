import json
import pandas as pd

tweets_data = []
for line in open('DATA.json',"r"):
    try:
        tweets_data.append(
            json.loads(line)
        )
    except:
        continue

tweets = pd.DataFrame()
tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)

print(tweets['lang'].value_counts())
print(tweets['country'].value_counts())
print(tweets['text'].value_counts())