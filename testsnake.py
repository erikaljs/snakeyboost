from machine import Pin
import neopixel
from time import sleep
import random
#déclarer les PIN
#mettre le sens des leds dans le meme

#init pin etc
pin = Pin(5, Pin.OUT) #initialise la broche GPIO
npx = neopixel(pin, 64) #on creer un neopixel par rapport a 64 pixels = le total
npx.write()

#init elem jeu
snake = [(3, 3)]  # position commencement serp
apple = (4,4)
dx, dy = 1,0#direction depart serpent 

def index(x, y):
    return y * 8 + x #conv donnees en index

def clear():
    for i in range(64):
        npx[i] = (0, 0, 0)  # LED éteinte
    npx.write()

#cette def permet d'avoir le meme sens pour les led elles vont de gauche à droite mais 1/2 va de droite à gauche
#vu que cest une sur deux on garde un sens et on change l'autre dans ce mm la pour la selectionner on utilise la methode de pair et impair 
def moveled(a, b, c, d):
    #for x in range(4, 1):  # commence à 4 et s'incrémente de 1
    for x in range(a,b) : 
        for y in range(c,d):
            if x %2 :#  si y est pair (%2)
                idx = index(x, 7-y)  # 7-y = pour inverser le sens sur y
                npx[idx] = (0,0,32)  # bleu
                npx.write()
                sleep(0.1)
            else :
                idx = index(x, y)  # Récupère l'index du pixel correspondant
                npx[idx] = (0,0,32)  # bleu
                npx.write()
                sleep(0.1)  # Pause de 0.1 seconde
                

def pos_apple(snake):
    global apple
    while True:
        x = random.randint(0, 7) #position random sur ligne 
        y = random.randint(0, 7) #position random sur colonne
        # verif pomme n'est pas sur le serpent
        if (x, y) != snake:
            apple = (x, y)
            idx = index(x, y)
            npx[idx] = (0, 255, 0)  # Couleur verte pour la pomme
            npx.write()
            break
#deplacer tete serpent 
def move_snake(dx, dy): #dx et dy = direction sur x et y
    global snake, apple # variable global = on peut y acceder mm en dehors de la fonction
    # position tete serp
    headx, heady = snake[-1] #-1 car on veut la tete
    pos_head = (headx + dx, heady + dy)#on additionne la position de base à la nouv dir)

    # Vérifie si le serpent a mangé la pomme
    if pos_head == apple:
        snake.append(pos_head)  # aug taille serpent 
        pos_apple(snake)  # pouf nouv pomme
    else:
        # Déplace le serpent
        snake.append(pos_head)
        snake.pop(0)  # Supprime la queue du serpent pour le déplacer
        
    # Affiche le serpent
    clear()
    for x, y in snake:
        idx = index(x, y)
        npx[idx] = (0, 0, 32)  # couleur serpent
    if apple:
        x, y = apple  
        idx = index(x, y)  
        npx[idx] = (0, 255, 0)
    npx.write()

def main():
    global dx, dy
    pos_apple(snake)  # Générer la première pomme

    while True:
        move_snake(dx, dy)  # Déplacer le serpent dans la direction actuelle

        # Ajouter un délai pour que le serpent se déplace à une vitesse raisonnable
        sleep(0.5)
