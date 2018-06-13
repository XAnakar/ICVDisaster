import csv,json

Entrada = open("DataSet.json")

Saida = csv.writer(open('names.csv', 'w'))
    
fieldnames = ['id', 'nome', 'data/hora','latitude','longitude','texto']

Saida.writerow(fieldnames)


for Linha in Entrada:
    Data = json.loads(Linha)
    
    Name = Data['nome']
    Id   = Data['id']
    Geo = Data['geo'].replace('[','').replace(']','').split(',')
    Hora = Data['data']
    Texto = Data['text']
    Salvar = [Id, Name, Hora, Geo[0], Geo[1], Texto]
    Saida.writerow(Salvar)

