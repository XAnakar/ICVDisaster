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



tweets['data'] = map(lambda tweet: tweet['data'], tweets_data)


'''
tweets['nome'] = map(lambda tweet: tweet['nome'], tweets_data)
tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
tweets['id'] = map(lambda tweet: tweet['id'], tweets_data)
tweets['geo'] = map(lambda tweet: tweet['geo'], tweets_data)
'''
print(tweets['data'].value_counts())
