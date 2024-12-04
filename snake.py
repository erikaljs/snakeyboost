from machine import Pin
import neopixel
from time import sleep
import random

#boutons 
bout_haut = Pin(6, Pin.IN, Pin.PULL_UP)   
bout_droite = Pin(20, Pin.IN, Pin.PULL_UP)
bout_gauche = Pin(22, Pin.IN, Pin.PULL_UP)  
bout_bas = Pin(23, Pin.IN, Pin.PULL_UP) 

#matrice
pin = Pin(5, Pin.OUT)  
'''
/!\ neopixel est un module et NeoPixel est une classe définie dans ce module.
On doit utiliser neopixel.NeoPixel pour créer une instance.
'''
npx = neopixel.NeoPixel(pin, 64)  # on creer un NeoPixel pour 64 pixels = total
npx.write()

# Position initiale
snake = [(3, 3)]  # pos  depart serpent 
apple = (4, 4)  # prem pomme random
dx, dy = 0, 0  #serpent bouge pas au debut 

#conv coord x y en index pour tab LEDs
def index(x, y):
    return y * 8 + x 

# etat boutons
def etat_boutons():
    global dx, dy
    if not bout_haut.value():  # si ce bouton pressé = serpent vers le haut 
        dx, dy = 0, -1  #haut
    elif not bout_droite.value():  
        dx, dy = 1, 0  #droite
    elif not bout_gauche.value():  
        dx, dy = -1, 0  # gauche
    elif not bout_bas.value():  
        dx, dy = 0, 1  # bas

def clear():
    for i in range(64):
        npx[i] = (0, 0, 0)  
    npx.write()

#pos pomme 
def pos_apple(snake):
    global apple
    while True:
        x = random.randint(0, 7)
        y = random.randint(0, 7)
        if (x, y) not in snake:  # faire en sorte que la pomme n'apparaisse pas sur le serpent directement 
            apple = (x, y)
            idx = index(x, y)
            npx[idx] = (0, 128, 0)  # vert
            npx.write()
            break


def draw():
    for x, y in snake:
        idx = index(x, y)
        npx[idx] = (0, 0, 32)  #bleu serp
    x, y = apple
    idx = index(x, y)
    npx[idx] = (0, 32, 0)  # vert pomme
    npx.write()

# dep serpent avec collisions mouv
def move_snake(dx, dy):
    global snake, apple
    headx, heady = snake[-1]

    # calc pos tête
    new_headx = (headx + dx) % 8  # % modulo a vec nb pixel permet que il ne dep pas la grilel
    new_heady = (heady + dy) % 8

    pos_head = (new_headx, new_heady)

    # si le sero se touche 
    if pos_head in snake:
        print("Game over, votre serpent s'est mordu!")
        return False

    # serp sur pomm
    if pos_head == apple:
        snake.append(pos_head)  # +1 corps
        pos_apple(snake)  # nouv pomme
    else:
        snake.append(pos_head)  # dep du serpent +1 sur la tête pour simuler le déplacement
        snake.pop(0)  # suppression de la dernière LED du corps pour simuler le déplacement

    # maj
    clear()
    draw()
    return True

def main():
    global dx, dy
    pos_apple(snake)  #prem pomme
    draw() 
    print("appyez sur un bouton")

    # joueur boutons
    while dx == 0 and dy == 0:
        etat_boutons()  # Vérifie l'état des boutons
        sleep(0.1)  

    print("start")

    while True:
        etat_boutons()  
        if not move_snake(dx, dy):  # stop collision
            print("foin ")
            break
        sleep(0.2)  


main()
