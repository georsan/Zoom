import json

f=open("horario.json","r")
contenido= f.read()
horario=json.loads(contenido)
for dia in horario["Friday"]:
    print(dia[""])      

