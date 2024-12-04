from machine import Pin, PWM
import time

pwmG1 = PWM(Pin(23), freq=5000, duty_u16=32768) # create PWM object from a pin
pwmG2 = PWM(Pin(22), freq=5000, duty_u16=32768)
pwmD1 = PWM(Pin(16), freq=5000, duty_u16=32768) # create PWM object from a pin
pwmD2 = PWM(Pin(17), freq=5000, duty_u16=32768)
en = Pin(25, Pin.OUT)
en.on() # on déclare le enable à l'état haut .on = une sortie 
#duty = pwmG.duty()         # get current duty cycle, range 0-1023 (default 512, 50%)


def gauchefull():
  pwmG1.duty(500) # sets the digital pin 13 on // quand on utilise analogWrite cest donc quon utilise une plage de l=valeur qui signifie quon utilise PWM
  pwmG2.duty(0)
  pwmD1.duty(500) # sets the digital pin 13 on
  pwmD2.duty(0)

def gauchesmooth():
  pwmG1.duty(500) # sets the digital pin 13 on // quand on utilise analogWrite cest donc quon utilise une plage de l=valeur qui signifie quon utilise PWM
  pwmG2.duty(0)
  pwmD1.duty(0) # sets the digital pin 13 on
  pwmD2.duty(500)
 


def stop():
  pwmG1.duty(500) # sets the digital pin 13 on // quand on utilise analogWrite cest donc quon utilise une plage de l=valeur qui signifie quon utilise PWM
  pwmG2.duty(500)
  pwmD1.duty(500) # sets the digital pin 13 on
  pwmD2.duty(500)
 # on envoie des 500 partout car les moteurs tournent que si on a un differentiel

def avance():
  pwmG1.duty(500) # sets the digital pin 13 on // quand on utilise analogWrite cest donc quon utilise une plage de l=valeur qui signifie quon utilise PWM
  pwmG2.duty(0)
  pwmD1.duty(0) # sets the digital pin 13 on
  pwmD2.duty(500)


def recule():
  pwmG1.duty(0) # sets the digital pin 13 on // quand on utilise analogWrite cest donc quon utilise une plage de l=valeur qui signifie quon utilise PWM
  pwmG2.duty(500)
  pwmD1.duty(500) # sets the digital pin 13 on
  pwmD2.duty(0)



def gauche():
  pwmG1.duty(500) # sets the digital pin 13 on // quand on utilise analogWrite cest donc quon utilise une plage de l=valeur qui signifie quon utilise PWM
  pwmG2.duty(0)
  pwmD1.duty(0) #// sets the digital pin 13 on
  pwmD2.duty(0)
 

def droitchacal():
  pwmG1.duty(0) #// sets the digital pin 13 on // quand on utilise analogWrite cest donc quon utilise une plage de l=valeur qui signifie quon utilise PWM
  pwmG2.duty(0)
  pwmD1.duty(0) #// sets the digital pin 13 on
  pwmD2.duty(500) 
 

while True :
    print(en.value())#valeur du enable
    avance()
    time.sleep(2)
    recule()
    time.sleep(2)
```