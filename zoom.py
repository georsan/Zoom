import pyautogui 
import datetime
import time
import webbrowser
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



iniciar()