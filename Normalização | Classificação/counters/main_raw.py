import json
import pandas as pd

tweets_data = []
for line in open('RESULT.json',"r"):
    try:
        tweets_data.append(
            json.loads(line)
        )
    except:
        continue

tweets = pd.DataFrame()

tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
tweets['id'] = map(lambda tweet: tweet['id'], tweets_data)
tweets['geo'] = map(lambda tweet: tweet['geo'], tweets_data)

print(tweets['geo'].value_counts())