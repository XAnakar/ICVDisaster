import json

def  get_Specific_Id(param, query):
    
    for __ in open(param,"r"):
        tweet = json.loads(__)
        if tweet['created_at'] == query:
            return tweet['id']
    return None


def get_Last_id(param):
    
    __id = None
    for __ in open(param,"r"):
        tweet = json.loads(__)
        __id  = tweet['id']
    return __id
