# -*- coding: utf-8 -*-

import json
import csv
import sys

saida = csv.writer(open('result.csv', 'w'))

fieldnames = ["id", "name", "text", "desc", "country", "lang", "city", "geo"]

saida.writerow(fieldnames)


# Verifica se a String por parâmetro se repete no csv ['formated.csv'], caso sim return True
def count_query(query):
    with open('result.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for line in reader:
            if line['text'] == query:
                return True
    return False


# Grava no arquivo csv ['formated.csv'] de acordo com o retorno da função  count_query
def make_csv():

    for line in open('DATA.json'):
        data = json.loads(line)

        if count_query(data['text']):
            print("Ocorrência!")
        else:
            if data['geo'] == "Unidentified":
                geo = "Unidentified,Unidentified".split(",")
            else:
                geo = data['geo']
            saida.writerow([data['id'], data['name'], data['text'], data['desc'], data['country'], data['lang'], data['city'], geo[0], geo[1]])



if __name__ == "__main__":
    make_csv()
