import json, csv

index = 0
Saida = csv.writer(open('formated.csv', 'w'))

fieldnames = ['id_str', 'screen_name', 'created_at','latitude','longitude','text']
Saida.writerow(fieldnames)

for Index in open("data_new.json"):

    Dados = json.loads(Index)
    Geo   = Dados['geo'].replace("[","").replace("]","").split(',')
    Saida.writerow([Dados['id'], Dados['nome'], Dados['data'], Geo[0], Geo[1], Dados['text']])
    
    print("[\x1B[35m",index,"\x1B[0m] - User: \x1B[33m"+ Dados['nome'] + "\x1B[0m Texto: \x1B[32m"+(Dados["text"].replace("\n",""))+"\x1B[0m")
    index += 1




    





    