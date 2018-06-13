#!/usr/bin/python
import json, csv, os, time

Arquivo = input('Nome do Arquivo + Extensão (Ex: file.txt): ')

Tweets = open(Arquivo, "r")
Eskreve = open("Data.json","w")

for line in Tweets:
	try:
		t = json.loads(line)
		if t["geo"]:  #Só entra se tiver Localização ativa
			Eskreve.write(line)
	except:
		continue
print("Concluído! . . .")
