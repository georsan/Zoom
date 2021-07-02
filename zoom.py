import pyautogui 
import datetime
import webbrowser
import json
from datetime import datetime
import time


def iniciar(url,clave):
    webbrowser.open(url,new=1,autoraise=True)       
    while True:
        reunion=pyautogui.locateOnScreen('./img/reunion.png')
        if reunion is None:            
            print('No click')
        else:
            pyautogui.click(reunion)
            print('Click')
            unir(clave)
            break

def unir(clave):
    while True:
        join=pyautogui.locateOnScreen('./img/password.png')
        print(join)
        if join is None:            
            print('No clave')
        else:
            pyautogui.typewrite(clave)
            pyautogui.click(pyautogui.locateOnScreen('./img/join.png'))
            print('Clave')
            break

hora=datetime.now().time()
hoy=datetime.today().strftime('%A')
horario=json.loads(open("horario.json","r").read())
for dia in  horario[hoy]:    
    if hora.strftime('%H')=="09":
        Data=horario[hoy][dia]
        Link=Data[0]["Link"]
        Contraseña=Data[0]["Contraseña"]
        iniciar(Link,Contraseña)
        time.sleep(7200)

    else:
        print("no")
        proximo=int(dia)*60-((hora.hour*60+hora.minute)*60+hora.second)
        if proximo>=0:
            time.sleep(proximo)
        else:
            break
    #Link=dia["Link"]
    #clave=dia["Contraseña"]       
