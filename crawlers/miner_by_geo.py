from twitter import *
import sys, csv, json, time

 
latitude    =   00
longitude   =   00    
max_range   =   00 #Km²

access_token        = 'chave'
access_token_secret = 'chave'
consumer_key        = 'chave'
consumer_secret     = 'chave'


twitter = Twitter(auth = OAuth(access_token, access_token_secret,consumer_key, consumer_secret))
Saida = open("data.json","a")

result_count = 0
while True:
    try:
        query = twitter.search.tweets(q = "", geocode = "%f,%f,%dkm" % (latitude, longitude, max_range), count = 100, max_id = last_id)
        
        for result in query["statuses"]:
            
            Data    = result['created_at']
            Name    = result['user']['screen_name']
            
            print('Usuário: '+ Name + '\nData:' + Data + '\n')

            Saida.write(str(json.dumps(result)) + "\n")
            result_count += 1

    except:
        
        print("Minerados até o momento -> [\x1b[31m%d\x1b[0m] Tweets..." % result_count)
        print("Timeout Requests API...")
        print("\x1b[31mEsperando...\x1b[0m 15 min")
        
        time.sleep(15 * 60)
        
        continue
