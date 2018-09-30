from twitter import *
import sys, csv, json, time



latitude    =   -0.893053	  
longitude   =  119.881364      
num_results =   50000000         
max_range   =   150 #Km²



access_token = 	'191826083-PNuKyQanN6pkOWbYtAo3vGFOxFHgxIf6C86Ds4RY'
access_token_secret = 'EL3jqr0L7B6yvZBDdzRN7rQhlFHXbrpwQTYcM8cg0DJ1A'
consumer_key = 'Aduzlaro6x41x2KeQzSaT8rT4'
consumer_secret = 'gX9U2HKaEo8xeJyURTI9NP73Q2BHswTbGpOggv5jUbWiRiDJlE'

twitter = Twitter(auth = OAuth(access_token, access_token_secret,consumer_key, consumer_secret))


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
