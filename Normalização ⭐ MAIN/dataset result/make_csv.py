# -*- coding: utf-8 -*-

import json, csv, sys

saida = csv.writer(open('formated.csv', 'w'))
fieldnames = ['id_str', 'screen_name', 'created_at','latitude','longitude','text']
saida.writerow(fieldnames)


#Verifica se a String por parâmetro se repete no csv ['formated.csv'], caso sim return True
def count_query(query):
    with open('formated.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for line in reader:
            if line['text'] == query:
                return True
    return False


#Grava no arquivo csv ['formated.csv'] de acordo com o retorno da função  count_query
def make_csv():

    for line in open('data_new.json'):
        data = json.loads(line)

        if count_query(data['text']):
            print("Ocorrência!")
        else:
            geo   = data['geo'].replace("[","").replace("]","").split(',') 
            saida.writerow([data['id'], data['nome'], data['data'], geo[0], geo[1], data['text']])

if __name__ == "__main__":
    make_csv()