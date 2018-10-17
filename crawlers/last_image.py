import json

def  get_lastId(param):
    
    for __ in open(param,"r"):
        tweet = json.loads(__)
        idd  = tweet['created_at']
        if idd[:11] == "Sat Oct 13 ":
            return tweet['id']
    return None
