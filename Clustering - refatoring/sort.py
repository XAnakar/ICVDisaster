import json
import csv


for line in open("CLUSTER.json"):

    tweet = json.loads(line)
    data = tweet['geos']
    data = sorted(data, key=lambda i: i[0])

    print(data)



#cluster teminado :) <3