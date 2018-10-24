# -*- coding: utf-8 -*-

import json, csv

saida = csv.writer(open('COL_TEXT.csv', 'w'))

fieldnames = ["text"]

saida.writerow(fieldnames)

def make_csv():

    for line in open('RESULT.json'):
        data = json.loads(line)
        saida.writerow([data['text']])


if __name__ == "__main__":
    make_csv()
