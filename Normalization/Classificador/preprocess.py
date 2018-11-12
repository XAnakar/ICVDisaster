from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
from nltk import  RegexpTokenizer
import re


def regex_clean_ruidos(text):
    return ' '.join([
        t for t in text.strip().split() if re.match(r'[^\W\d]*$', t)
    ])


def regex_clean(text):
    return regex_clean_ruidos(
        ' '.join(RegexpTokenizer(r'\w+').tokenize(text)).lower()
    )


def make_tokens(text):
    
    stop_words = set(stopwords.words('english')) 
    
    word_tokens = word_tokenize(
        regex_clean(text) #Vai tirar algumas impurezas do texto, como números e alguns simbolos
    ) 
    
    filtered_sentence = [w for w in word_tokens if not w in stop_words] 
    
    filtered_sentence = [] 
    
    for w in word_tokens: 
        if w not in stop_words: 
            filtered_sentence.append(w) 
    return filtered_sentence
