
from preprocess import preprocess #Faz manter toda @  ou # ligado à um nome
from collections import Counter
import string, operator, json

'''
#pre-processing exemplo
tweet = 'RT @marcobonzanini: just an example! :D http://example.com #NLP'
print(preprocess(tweet))
'''

with open('data_new.json', 'r') as f:
    
    count_all = Counter()
    
    for line in f:
        
        tweet = json.loads(line)

        terms_single = set(
            [term for term in preprocess(tweet['text'])]
        )
        
        terms_hash = [
            term for term in preprocess(tweet['text']) 
            if term.startswith('#')
        ]
    
        count_all.update(terms_hash)

    print(count_all.most_common(100))