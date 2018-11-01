
from tqdm import tqdm
import csv
import json
from time import sleep

SaidaClusters = open("CLUSTER.json", "w")

csv_file = open("RESULT.csv", "r")

geos = []

clusters = {}

Indentificares = [
    data['id_str'] for data in csv.DictReader(
        csv_file
    )
]

for index in tqdm(set(Indentificares)):

    counts = 0

    for data in csv.DictReader(open("RESULT.csv", "r")):

        if data['id_str'] == str(index):
            geos.append([data['created_at'][8:19].replace(
                ":", " "
                ), data['latitude'], data['longitude']]
            )  # Considerando a data
            counts += 1

    Insert = json.dumps({"id": str(index), "geos": geos, "count": counts})
    SaidaClusters.write(str(Insert)+"\n")
    geos = []

print("Clusterização Terminada!")
