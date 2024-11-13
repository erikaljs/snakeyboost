from libimport import *

pin = Pin(5, Pin.OUT)  # Initialise la broche GPIO
npx = neopixel.NeoPixel(pin, 64)  # Crée un NeoPixel avec 8 pixels

def index(x, y):
    return x * 8 + y
    
def moveled(a, b, c, d):
    #for x in range(4, 1):  # commence à 4 et s'incrémente de 1
    for x in range(a,b) : 
        for y in range(c,d):
            if x %2 :#  si y est pair (%2)
                idx = index(x, 7-y)  # 7-y = pour inverser le sens sur y
                npx[idx] = (0,0,32)  # bleu
                npx.write()
                sleep(0.1)
            else  :
                idx = index(x, y)  # Récupère l'index du pixel correspondant
                npx[idx] = (0,0,32)  # bleu
                npx.write()
                sleep(0.1)  # Pause de 0.1 seconde

def clear():
    npx.fill((0, 0, 0))  # Éteint tous les pixels
