import json
import pandas as pd

tweets_data = []

import csv
with open('RESULT.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        tweets_data.append(
            row['created_at']
        )

tweets = map(lambda tweet: tweet, tweets_data)

new = []

for t in tweets:
    new.append(t[8:19].replace(":"," "))


for line in range(20):
    print(new[line])
print("---------------")
new.sort()
for line in range(20):
    print(new[line])