import csv, json
from time import sleep
from bar import printProgressBar

SaidaClusters = open("Clusters.json","w")

csv_file = open("formated.csv","r")

Indentificares = [
    data['id_str'] for data in csv.DictReader(
        csv_file
    )
]

geos = []
clusters = {}

for index in set(Indentificares):
   
    counts = 0

    for data in csv.DictReader(open("formated.csv","r")):
        if data['id_str'] == str(index):
            geos.append([data['created_at'], data['latitude'],data['longitude']])
            counts += 1
    Insert = json.dumps({"id":str(index), "geos":geos, "count":counts})
    SaidaClusters.write(str(Insert)+"\n")
    geos = []

print("Clusterização Terminada!")
