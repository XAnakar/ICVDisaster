# -*- coding: utf-8 -*-

import json, csv, sys

saida = csv.writer(open('formated.csv', 'w'))
fieldnames = ['id_str', 'screen_name', 'created_at','latitude','longitude','text']
saida.writerow(fieldnames)

def hit(query):
    with open('RESULT.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for line in reader:
            if line['text'] == query:
                return True
    return False

def make_csv():

    for line in open('DATASET.json'):
        data = json.loads(line)

        if hit(data['text']):
            print("Ocorrência!")
        else:
            geo   = data['geo'].replace("[","").replace("]","").split(',') 
            saida.writerow([data['id'], data['nome'], data['data'], geo[0], geo[1], data['text']])

if __name__ == "__main__":
    make_csv()