from libimport import *

#comme ca circulait pas dans le meme sens un coup sur deux on a tout mis dans le meme sens grace a la def moveled
def moveled():
    #for x in range(4, 1):  # commence à 4 et s'incrémente de 1
    for x in range(8) : 
        for y in range(8):
            if x %2 :#  si y est pair (%2)
                inversens()
                sleep(0.1)
            else  :
                sens()
                sleep(0.1)  # Pause de 0.1 seconde