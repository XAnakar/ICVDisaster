from twitter import *
import sys, csv, json, time

 
latitude    =   29.004037
longitude   =   -82.612344    
max_range   =   620 #Km²

access_token        = '829344089829158914-l3r3pDNPOP1o3Ada4ZuqUR6CPd9ZXqe'
access_token_secret = '97QwhsAsYkFAffPn8lrXuT7yK7XVRUcKdPGYRayJWTIn8'
consumer_key        = 'tCkkQCZadJqfh4jWUJZYGvCaj'
consumer_secret     = 'CvazdJkGaTwM053bAwd1h9K822643h4jblj7byRzNYqDoG7EuO'


twitter = Twitter(auth = OAuth(access_token, access_token_secret,consumer_key, consumer_secret))
Saida = open("data.json","a")

result_count = 0
while True:
    try:
        query = twitter.search.tweets(q = "", geocode = "%f,%f,%dkm" % (latitude, longitude, max_range), count = 100, max_id = last_id)
        
        for result in query["statuses"]:
            
            Data    = result['created_at']
            Name    = result['user']['screen_name']
            
            print('Usuário: '+ Name +"\n" + Data+"\n")

            Saida.write(str(json.dumps(result)) + "\n")
            result_count += 1

    except:
        
        print("Minerados até o momento -> [\x1b[31m%d\x1b[0m] Tweets..." % result_count)
        print("Timeout Requests API...")
        print("\x1b[31mEsperando...\x1b[0m 15 min")
        
        time.sleep(15 * 60)
        
        continue

