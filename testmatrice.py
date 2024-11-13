from machine import Pin
import neopixel
import time

pin = Pin(5, Pin.OUT)  # Initialise la broche GPIO
npx = neopixel.NeoPixel(pin, 8)  # Crée un NeoPixel avec 8 pixels

#npx[0] = (0, 0, 0)
#npx[1] = (0, 0, 0)
#npx[2] = (0, 0, 0)
#npx[3] = (0, 0, 0)# Violet
#npx[4] = (0, 0, 0)
#npx[5] = (0, 0, 0)
#npx[6] = (0, 0, 0)
#npx[7] = (0, 0, 0)
#npx.write()
# npx.fill((0, 0, 0))  #Remplir tous les pixels avec la même couleur
def index(x, y):
    return x * 8 + y

def moveled():
    for x in range(8):  # Parcours des 8 lignes
        for y in range(8):  #  8 colonnes
            npx.fill((0, 0, 0))  # Éteint tous les pixels
            idx = index(x, y)  # Récupère l'index du pixel correspondant
            npx[idx] = (0, 0, 32)  # bleu
            npx.write() 
            time.sleep(0.1)  # Pause de 0.1 seconde


moveled()
