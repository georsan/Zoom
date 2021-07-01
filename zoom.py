import pyautogui 
import datetime
import webbrowser
import json
from datetime import datetime
import time
import calendar


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

hora=datetime.now()
hoy=datetime.today().strftime('%A')
horario=json.loads(open("horario.json","r").read())
for dia in  horario[hoy]:    
    if hora.strftime('%H')==dia:
        Data=horario[hoy][dia]
        Link=Data[0]["Link"]
        Contraseña=Data[0]["Contraseña"]
        iniciar(Link,Contraseña)
        time.sleep(7200)

    else:
        print("no")
        print()

    #Link=dia["Link"]
    #clave=dia["Contraseña"]       
