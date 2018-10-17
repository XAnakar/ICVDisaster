import json

def  get_Specific_Id(param):
    
    for __ in open(param,"r"):
        tweet = json.loads(__)
        idd  = tweet['created_at']
        if idd[:11] == "Sat Oct 13 ":
            return tweet['id']
    return None


def get_Lest_id(param):
    
    __id = None
    for __ in open(param,"r"):
        tweet = json.loads(__)
        id  = tweet['id']

     return __id
