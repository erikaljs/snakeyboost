from machine import Pin
import neopixel

pin = Pin(5, Pin.OUT)
npx = neopixel.NeoPixel(pin, 64)

npx[0] = (32, 0, 0)
npx.write()
