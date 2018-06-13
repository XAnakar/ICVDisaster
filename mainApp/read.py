import json

xfile = input("Nome + Extensão do Arquivo:[arquivo.csv]: ")
index = 1
for Index in open(xfile):
    Dados = json.loads(Index)
    
    #Text  = Dados["text"].replace("\n","").replace("https://t.co/","")
    #Text  = Text[0:len(Text) - 12]
    print("[\x1B[35m",index,"\x1B[0m] - User: \x1B[33m"+ Dados['user']['screen_name'] + "\x1B[0m Texto: \x1B[32m"+(Dados["text"].replace("\n",""))+"\x1B[0m")
    index += 1


