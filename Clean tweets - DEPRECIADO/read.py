#-*- coding: utf-8 -*-
import json, string
from collections import Counter

arq = open('texto_limpo.txt', 'r')
texto = arq.read()
palavras = texto.split(' ')
contador = Counter(palavras)

for i in contador.items():
    print(i)
arq.close()
