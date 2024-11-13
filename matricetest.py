from libimport import *

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

'''
sert a inverser sens index 
def order(x,y):
    if y %2 == 0 :
        return y * 8 + x
    else:
        return y *8 + (7-x)
 '''    
                
while True : # (0,8 cest la base) 1-colonne où il va commencer 2- numéo de la colonne sur laquelle il va s'arreter 3 et 4 pareil mais pour les lignes 
    moveled(0,1,2,5)
    moveled(3,4,3,4)
    moveled(7,8,2,5)

