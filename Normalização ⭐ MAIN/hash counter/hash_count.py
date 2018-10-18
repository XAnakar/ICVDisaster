from collections import Counter
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import json


def get_hashtags(tweet):

    entities = tweet.get('entities', {})
    hashtags = entities.get('hashtags', [])

    return [tag['text'].lower()  for tag in hashtags]

objects = []
performance = []


import chardet


if __name__ == "__main__":

    with open("DATA.json","r") as f:
        hashtags = Counter()
        for line in f:

            tweet = json.loads(line)
            hashtags_in_tweet = get_hashtags(tweet)
            hashtags.update(hashtags_in_tweet)
        
        for tag, count in hashtags.most_common(10):

            objects.append(tag)
            performance.append(count)
            print(tag,"-->", count)


y_pos = np.arange(len(objects))
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Quantidade')
plt.title('hashtags')
 
plt.show()