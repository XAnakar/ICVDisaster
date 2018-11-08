import json
import csv
from preprocess import make_tokens
from query import mainz

bag_of_words = [line.lower().replace("\n","") for line in open('base.txt')]
c = 0
for line in open('RESULT.json'):
    data = json.loads(line)

    if mainz(bag_of_words, make_tokens(data['text'])):
        print(data['text'])
        c += 1    

bag_of_words.sort()
print(bag_of_words)


print("Quantos?:",c)