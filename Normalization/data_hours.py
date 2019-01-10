import csv

data = [line['created_at'] for line in csv.DictReader(open("RESULT.csv"))]

data.sort(key=lambda k: k[4:19])

print(min(data) +" à "+ max(data))