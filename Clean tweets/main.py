# encoding=utf8
import sys, re, json, emoji

reload(sys)
sys.setdefaultencoding('utf8')

arq = open("texto_limpo.txt", "w")

def remove(text):
    allchars = [str for str in text.decode('utf-8')]
    emoji_list = [c for c in allchars if c in emoji.UNICODE_EMOJI]
    clean_text = ' '.join([str for str in text.decode('utf-8').split() if not any(i in str for i in emoji_list)])
    return clean_text


for line in open("DataSet.json"):

    data = json.loads(line)
    texto = data['text'].replace("\n","") #substitui quebra de linha por espaço
    texto = remove(texto) #remove todos os emojis
    print(texto)
    arq.write(str(texto))


arq.close() 