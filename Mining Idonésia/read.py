import json

index = 0
with open("data.json","r") as f:

    for line in f:
        tweet = json.loads(line)
        print(index,'->>',tweet['text'].replace("\n",""))
        index += 1
