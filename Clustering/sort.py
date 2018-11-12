import json
import csv

count = 0
for line in open("CLUSTER.json"):

    tweet = json.loads(line)
    data = tweet['geos']
    data.sort(key=lambda k: k[0][4:19])
    print('----------------------')
    for line in data:
        print(line)
    print('----------------------')
