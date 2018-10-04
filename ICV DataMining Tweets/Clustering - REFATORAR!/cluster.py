import csv, json

SaidaClusters = open("Clusters.json","w")
dataSet = csv.DictReader(open("names.csv","r"))
Indentificares = []
for data in dataSet:
    Indentificares.append(data['id'])

geos = []
clusters = {}

for index in set(Indentificares):
    counts = 0
    for data in csv.DictReader(open("names.csv","r")):
        if data['id'] == index:
            geos.append([data['latitude'],data['longitude']])
            counts += 1
    Insert = json.dumps({"id":str(index),"geos":geos,"count":counts})
    SaidaClusters.write(str(Insert)+"\n")
    print("- ")
    geos = []
print("Clusterização Terminada!")