from twitter import *
import sys, csv, json, time



latitude    =   0	  
longitude   =   0       
num_results =   0           
max_range   =   0 #Km²


twitter = Twitter(auth = OAuth('chave',
            'chave',
            'chave',
            'chave'))

Saida = open("DataSet.json","a")

result_count = 0
last_id = None

while result_count <  num_results:
    try:
        query = twitter.search.tweets(q = "", geocode = "%f,%f,%dkm"
                            % (latitude, longitude, max_range),
                            count = 100, max_id = last_id)

        for result in query["statuses"]:
            if result["geo"]:
                
                Id     = result['user']['id']
                Data   = result['created_at']
                #Tratamento de texto msg
                Mensagem  =  result["text"].replace("\n","").replace("https://t.co/","") #substitui "\n" por ""
                Mensagem  =  Mensagem[0:len(Mensagem) - 12]
                #FimTratamento

                Name   = result['user']['screen_name']
                Coords = result['geo' ]['coordinates']

                print('Identificado: \x1b[32m'+str(Id)+'\x1b[0m\nUsuário: \x1b[32m'+ str(Name)+'\x1b[0m\nData/Hora: \x1b[32m'+str(Data)+'\x1b[0m\nTexto: \x1b[32m'+str(Mensagem)+'\x1b[0m\nCoordinates: \x1b[32m'+str(Coords)+'\x1b[0m\n')

                Insert = json.dumps({
                    "id":str(Id),
                    "data":str(Data),
                    "text": Mensagem,
                    "nome": Name,
                    "geo": str(Coords)
                })
                
                Saida.write(str(Insert) + "\n")
                result_count += 1
            last_id = result["id"]
    except:
        print("Minerados até o momento -> [\x1b[31m%d\x1b[0m] Tweets..." % result_count)
        print("Timeout Requests API...")
        print("\x1b[31mEsperando...\x1b[0m 15 min")
        time.sleep(15 * 60)
        continue
