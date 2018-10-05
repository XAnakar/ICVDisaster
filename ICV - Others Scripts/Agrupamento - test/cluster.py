import json

struct = [(json.loads(Index)['id']) for Index in open("entrada.json", "r")]

Data  = open("entrada", "r")

Saida = open("saida.json", "w")

Indice = 0
obj = []

for Line in Data:
    Tweet  = json.loads(Line)
    try:
        Search = struct[Indice]
    except:
        pass
    Name   = Tweet['nome']
    Coords = Tweet['geo']
    
    counts = struct.count(Search)

    for Index in struct:
        if Search == Index:
            obj.append(Coords)
            struct.remove(Search)
  
    if counts > 1:
        Insert = json.dumps({"id":str(Search),"Nome":Name,"Geo":obj,"Count":counts})
        Saida.write(str(Insert)+"\n")
    obj = []
    Indice += 1


Saida.close()
Data.close()
