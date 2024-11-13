from machine import Pin
import neopixel   

pin = Pin(5, Pin.OUT) #initialise la broche GPIO
npx = neopixel(pin, 8) #on creer un neopixel par rapport a 8 pixel
npx[0] = (255,0,255) #violet et (34,222,177) = bleu clair
npx.write()
r, g, b = npx[0]
#npx.fill((255,255,255)) = met tt les pixel dans cette couleur la 
