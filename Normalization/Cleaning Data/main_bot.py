# -*- coding: utf-8 -*-

import json
import csv
import sys
from tqdm import tqdm
from ignored import ignored

saida = csv.writer(open('RESULT.csv', 'w'))
fieldnames = ['id_str', 'screen_name',
              'created_at', 'latitude', 'longitude', 'text']
saida.writerow(fieldnames)
saida2 = open("RESULT.json", "w")


def make_csv():

    ignored_bots = [line.lower().replace("\n", "") for line in open('blacklist.txt')]
 
    for line in tqdm(open('RESULT_DUP.json')):
        data = json.loads(line)

        # Caso o Tweet se repita ou se o usuário seja um perfil bot
        if ignored(ignored_bots, data['nome']) == False:
            saida2.write(str(json.dumps(data))+"\n")
            geo = data['geo'].replace("[", "").replace("]", "").split(',')

            saida.writerow([
                data['id'],
                data['nome'],
                data['data'],
                geo[0],
                geo[1],
                data['text']]
            )


if __name__ == "__main__":
    make_csv()
