from twitter import *
import sys, csv, json, time
from last_id import  get_Last_id


latitude    =   00
longitude   =   00
max_range   =   00 #Km^2

consumer_key        = 'chave'
consumer_secret     = 'chave'
access_key          = 'chave'
access_secret       = 'chave'


twitter = Twitter(auth = OAuth(access_key, access_secret,consumer_key, consumer_secret))
Saida = open("DATA_SET.json","a")

result_count = 0
last_id =  get_Last_id("DATA_SET.json")

while True:
    try:
        query = twitter.search.tweets(q = "", geocode = "%f,%f,%dkm" % (latitude, longitude, max_range), count = 200, max_id = last_id)
    
        for result in query["statuses"]:
            
            Id     = result['user']['id']
            Date   = result['created_at']
            Mensagem  =  result["text"].replace("\n","")
            Name   = result['user']['screen_name']
            Lang   = result['lang']
    
            if result['user']['description'] != None:
                Desc = result['user']['description']
            else:
                Desc = "Unidentified"
    
            if result['geo'] != None:
                Coords = result['geo']['coordinates']
            else:
                Coords = "Unidentified"
                
            if result['place'] != None:
                City    =  result['place']['full_name']
                Country =  result['place']['country'] 
            else:
                City    = "Unidentified"
                Country = "Unidentified" 
    
            
            print('Identificado: '+str(Id)+'\nUsuário: '+ str(Name)+'\nData/Hora: '+str(Date)+'\nTexto: '+str(Mensagem)+'\nCoordinates: '+str(Coords)+'\n')
    
            Insert = json.dumps({
    
                "id": Id,
                "date": Date,
                "text": Mensagem,
                "name": Name,
                "lang": Lang,
                "desc": Desc,
                "geo":  Coords,
                "country": Country,
                "city": City,
            })

            Saida.write(str(Insert) + "\n")
            result_count += 1
                
            last_id = result["id"]
    except:
        
        print(" Minerados até o momento -> [\x1b[31m%d\x1b[0m] Tweets..." % result_count)
        print(" Timeout Requests API... ")
        print(" \x1b[31mEsperando...\x1b[0m 15 min ")
        time.sleep(15 * 60)
        continue
