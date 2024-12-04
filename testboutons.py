from machine import Pin
import neopixel
from time import sleep


bout_haut = Pin(6, Pin.IN, Pin.PULL_UP)  
bout_droite = Pin(20, Pin.IN, Pin.PULL_UP) 
bout_gauche = Pin(22, Pin.IN, Pin.PULL_UP)   
bout_bas = Pin(23, Pin.IN, Pin.PULL_UP)  


pin = Pin(5, Pin.OUT)
npx = neopixel.NeoPixel(pin, 64) 


def index(x, y):
    return y * 8 + x


def clear():
    for i in range(64):
        npx[i] = (0, 0, 0)  
    npx.write()


def test_buttons():
    print("en cours")

    while True:
        if not bout_haut.value():
            print("haut")
            npx[index(3, 0)] = (255, 0, 0)  
        elif not bout_droite.value():  
            print("droite")
            npx[index(7, 3)] = (0, 255, 0)  
        elif not bout_gauche.value():  
            print("gauche")
            npx[index(0, 3)] = (0, 0, 255) 
        elif not bout_bas.value(): 
            print("bas")
            npx[index(3, 7)] = (255, 255, 0)  

        npx.write()  
        sleep(0.1)  

test_buttons()
