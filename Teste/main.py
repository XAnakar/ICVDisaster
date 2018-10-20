import json

for line in open('DATA.json',"r"):
    
    result = json.loads(line)

    Id     = result['user']['id']
    Date   = result['created_at']
    Mensagem  =  result["text"].replace("\n","")
    Name   = result['user']['screen_name']
    Lang   = result['lang']

    if result['user']['description'] != None:
        Desc = result['user']['description']
    else:
        Desc = "Unidentified"

    if result['geo'] != None:
        Coords = result['geo']['coordinates']
    else:
        Coords = "Unidentified"
        
    if result['place'] != None:
        City    =  result['place']['full_name']
        Country =  result['place']['country'] 
    else:
        City    = "Unidentified"
        Country = "Unidentified" 

    print('Identificado: '+str(Id)+'\nUsuário: '+ str(Name)+'\nData/Hora: '+str(Date)+'\nTexto: '+str(Mensagem)+'\nCoordinates: '+str(Coords)+'\n')