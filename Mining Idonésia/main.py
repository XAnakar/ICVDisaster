from twitter import *
import sys, csv, json, time


latitude    =   -1.153703
longitude   =   119.938673      
num_results =   900000000000000         
max_range   =   250 #Km²


access_token = 	      '191826083-dxxvkqc8KoRYm7JFT8ecla29Gyu7W2M64L8zT8Pd'
access_token_secret = 'TYKvdydWEm8og3IFeTfVV04clIweS8a7SrkiYG7cPddH5'
consumer_key =        'ibrxleGYanQ3bVn6Ms7PhUqFS'
consumer_secret =     'JlGkKbkOT0qhZhBprspwI1C5nOZ34u3HqBYfdZTITy2OeowuSi'


twitter = Twitter(auth = OAuth(access_token, access_token_secret,consumer_key, consumer_secret))


Saida = open("data.json","a")

result_count = 0
last_id = None

while result_count <  num_results:
    try:
        query = twitter.search.tweets(q = "", geocode = "%f,%f,%dkm"
                            % (latitude, longitude, max_range),
                            count = 100, max_id = last_id)

        for result in query["statuses"]:
            
            Id     = result['user']['id']
            Data   = result['created_at']

            Mensagem  =  result["text"].replace("\n","")

            Name   = result['user']['screen_name']
            Coords = result['geo' ]['coordinates']

            print('Identificado: \x1b[32m'+str(Id)+'\x1b[0m\nUsuário: \x1b[32m'+ str(Name)+'\x1b[0m\nData/Hora: \x1b[32m'+str(Data)+'\x1b[0m\nTexto: \x1b[32m'+str(Mensagem)+'\x1b[0m\nCoordinates: \x1b[32m'+str(Coords)+'\x1b[0m\n')

            
            Saida.write(str(json.dumps(result)) + "\n")
            result_count += 1
            last_id = result["id"]
    except:
        print("Minerados até o momento -> [\x1b[31m%d\x1b[0m] Tweets..." % result_count)
        print("Timeout Requests API...")
        print("\x1b[31mEsperando...\x1b[0m 15 min")
        time.sleep(15 * 60)
        continue
