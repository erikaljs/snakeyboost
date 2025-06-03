# dodge.py
import neopixel
from machine import Pin, ADC, PWM
from time import sleep
import random

class Buzzer:
    def __init__(self, pin=21):
        self.buzzer = PWM(Pin(pin, Pin.OUT))
        self.buzzer.duty(200)
        self.notes = [262,330,392,523,587,698,784,880]
    def play_note(self, f,d):
        self.buzzer.freq(f); self.buzzer.duty(200); sleep(d); self.buzzer.duty(0)
    def hit_bad(self):     self.play_note(self.notes[1],0.1)
    def collect_good(self):self.play_note(self.notes[5],0.1)
    def lose_life(self):   self.play_note(self.notes[2],0.2)
    def play_game_over_sound(self):
        for n in (2,1,0): self.play_note(self.notes[n],0.15)

class Joystick:
    def __init__(self, pin_x=15, pin_y=2):
        self.xAxis = ADC(Pin(pin_x)); self.xAxis.atten(self.xAxis.ATTN_11DB)
        self.yAxis = ADC(Pin(pin_y)); self.yAxis.atten(self.yAxis.ATTN_11DB)
    def read(self):
        return self.xAxis.read(), self.yAxis.read()

class Matrice:
    def __init__(self, pin=23):
        self.width = 16
        self.height = 8
        self.npx = neopixel.NeoPixel(Pin(pin, Pin.OUT), self.width * self.height)
    def get_led_index(self, x, y):
        if y % 2 == 0:
            return y * self.width + x
        else:
            return y * self.width + (self.width - 1 - x)
    def set_pixel(self, x, y, color):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.npx[self.get_led_index(x, y)] = color
    def clear(self):
        self.npx.fill((0,0,0))
    def write(self):
        self.npx.write()

class DodgeGame:
    def __init__(self):
        self.width = 16
        self.height = 8
        self.matrice = Matrice()
        self.joystick = Joystick()
        self.buzzer = Buzzer()
        self.player_y = 4
        self.lives = 3
        self.score = 0
        self.obstacles = []  # [x, y, type]
        self.spawn_rate = 0.2

    def spawn_obstacle(self):
        if random.random() < self.spawn_rate:
            y = random.randint(0, self.height - 1)
            t = 'good' if random.random() < 0.3 else 'bad'
            self.obstacles.append([self.width - 1, y, t])

    def move_obstacles(self):
        new = []
        for x,y,t in self.obstacles:
            x -= 1
            if x < 0:
                if t == 'good':
                    self.lives -= 1
                    self.buzzer.lose_life()
                continue
            new.append([x,y,t])
        self.obstacles = new

    def update_player(self):
        _, y = self.joystick.read()
        if y < 1000 and self.player_y > 0:
            self.player_y -= 1
        elif y > 3000 and self.player_y < self.height - 1:
            self.player_y += 1

    def check_collision(self):
        new = []
        for x,y,t in self.obstacles:
            if x == 0 and y == self.player_y:
                if t == 'bad':
                    self.lives -= 1
                    self.buzzer.hit_bad()
                else:
                    self.score += 1
                    self.buzzer.collect_good()
            else:
                new.append([x,y,t])
        self.obstacles = new

    def draw(self):
        self.matrice.clear()
        for i in range(self.lives):
            self.matrice.set_pixel(i, self.height-1, (0,10,0))
        self.matrice.set_pixel(0, self.player_y, (0,10,0))
        for x,y,t in self.obstacles:
            c = (10,0,0) if t=='bad' else (0,0,10)
            self.matrice.set_pixel(x, y, c)
        self.matrice.write()

    def run(self):
        while self.lives > 0:
            self.spawn_obstacle()
            self.move_obstacles()
            self.update_player()
            self.check_collision()
            self.draw()
            sleep(0.2)
        self.buzzer.play_game_over_sound()

def run_dodge():
    game = DodgeGame()
    game.run()

if __name__ == "__main__":
    run_dodge()
