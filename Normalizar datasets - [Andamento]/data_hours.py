import csv

data = [line['created_at'] for line in csv.DictReader(open("formated.csv"))]
data.sort()
print("Primeiro Tweet: ", data[0])
print("Ultimo Tweet: ", data[len(data) - 1])