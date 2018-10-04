import csv

saida = csv.writer(open('texts.csv', 'w'))

saida.writerow(["text"])

with open('formated.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for line in reader:
        print(line['text'])
        saida.writerow([line['text']]) 
