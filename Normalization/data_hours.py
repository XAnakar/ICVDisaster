import csv

data = [line['created_at'] for line in csv.DictReader(open("RESULT.csv", encoding="utf8"))]
data.sort()

print("Primeiro Tweet: ", min(data) + "\n" +
      "Ultimo Tweet: ", max(data)
)
