from twitter import *
import sys, csv, json, time
from last_id import  get_Last_id , get_size
import math

latitude    =   00
longitude   =   00
max_range   =   99999999999999999999999999999999999999999999999

consumer_key = "lD7L0yp96HNaW9KptvAobmLQm"
consumer_secret = "8NMFdjYGLmFx2MpNCbUlGkWyVx70GwLusk20iRP0cdfoLBa4Uf"
access_token_key = "1096656986530373632-hj8hJuiBZoSXAvAMpzvvIPDBgA5qis"
access_token_secret = "putuIQD8IGFAhiEshHoANO5pns7WA7WYA1U6edwxXI3gC"


twitter = Twitter(auth = OAuth(access_token_key, access_token_secret,consumer_key, consumer_secret))
Saida = open("DATA.json","a")

result_count = get_size("DATA.json")
last_id =  get_Last_id("DATA.json")

while True:
    try:
        query = twitter.search.tweets(q = "", geocode = "%f,%f,%dkm" % (latitude, longitude, max_range), count = 100, max_id = last_id)
    
        for result  in query["statuses"]:
            if result["geo"]:
                
                Id     = result['user']['id']
                Date   = result['created_at']
                Mensagem  =  result["text"].replace("\n","")
                Name   = result['user']['screen_name']
                Lang   = result['lang']
        
                if result['user']['description'] != None:
                    Desc = result['user']['description']
                else:
                    Desc = "NaN"
        
                if result['geo'] != None:
                    Coords = result['geo']['coordinates']
                else:
                    Coords = "NaN"
                    
                if result['place'] != None:
                    City    =  result['place']['full_name']
                    Country =  result['place']['country'] 
                else:
                    City    = "NaN"
                    Country = "NaN" 
        
                
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
