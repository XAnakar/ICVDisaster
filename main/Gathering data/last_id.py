import json

def get_Last_id(param):
    
    __id = None
    for __ in open(param,"r"):
        tweet = json.loads(__)
        __id  = tweet['id']
    return __id


def post(name):
	count = 0
	for line in open(name):
		count += 1
	return count
