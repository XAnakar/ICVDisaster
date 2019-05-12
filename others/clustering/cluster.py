
from tqdm import tqdm
import csv
import json
from time import sleep
from preprocess import make_tokens

SaidaClusters = open("CLUSTER.json", "w")


geos = []
Text = []
clusters = {}

Indentificares = [
    json.loads(data)['id'] for data in open("RESULT.json", "r")
]

for index in tqdm(set(Indentificares)):

    counts = 0

    for data in open("RESULT.json", "r"):
        data = json.loads(data)
        if data['id'] == str(index):

            geo = data['geo'].replace("[", "").replace("]", "").split(',')
            Text.append(data['text'])

            geos.append([data['data'], geo[0], geo[1]])  # Considerando a data
            counts += 1

    Insert = json.dumps({"id": str(index), "texts": make_tokens("".join(Text)), "geos": geos, "count": counts})
    SaidaClusters.write(str(Insert)+"\n")
    geos = []
    Text = []

print("Clusterização Terminada!")
