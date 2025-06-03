# snake.py
import neopixel
from machine import Pin, ADC, PWM
from time import sleep
import random

class Buzzer:
    def __init__(self, pin):
        self.buzzer = PWM(Pin(pin, Pin.OUT))
        self.buzzer.duty(200)
        self.notes = [262, 330, 392, 523, 587, 698, 784, 880]

    def play_note(self, frequency, duration):
        self.buzzer.freq(frequency)
        self.buzzer.duty(200)
        sleep(duration)
        self.buzzer.duty(0)

    def play_start_sound(self):
        self.play_note(self.notes[4], 0.3)
        self.play_note(self.notes[5], 0.3)
        self.play_note(self.notes[6], 0.3)

    def play_game_over_sound(self):
        self.play_note(self.notes[6], 0.3)
        self.play_note(self.notes[5], 0.3)
        self.play_note(self.notes[4], 0.3)

class Joystick:
    def __init__(self, pin_x, pin_y):
        self.xAxis = ADC(Pin(pin_x))
        self.xAxis.atten(ADC.ATTN_11DB)
        self.yAxis = ADC(Pin(pin_y))
        self.yAxis.atten(ADC.ATTN_11DB)

    def read(self):
        return self.xAxis.read(), self.yAxis.read()

class Matrice:
    def __init__(self, pin, width=8, height=16):
        self.width = width
        self.height = height
        self.npx = neopixel.NeoPixel(Pin(pin, Pin.OUT), width * height)

    def get_led_index(self, x, y):
        y = self.height - 1 - y
        if y % 2 == 0:
            return y * self.width + x
        else:
            return y * self.width + (self.width - 1 - x)

    def set_pixel(self, x, y, color):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.npx[self.get_led_index(x, y)] = color

    def update_display(self, snake, apple, applebeurks=None):
        self.npx.fill((0, 0, 0))
        for x, y in snake:
            self.set_pixel(x, y, (0, 10, 0))  # vert
        self.set_pixel(*apple, (10, 0, 0))   #rouge
        if applebeurks:
            for ab in applebeurks:
                self.set_pixel(*ab.position, (10, 5, 0))  #oange
        self.npx.write()

class AppleBeurk:
    def __init__(self, snake, width, height, apple):
        self.position = self.generate_position(snake, width, height, apple)

    def generate_position(self, snake, width, height, apple):
        pos = (random.randint(0, width - 1), random.randint(0, height - 1))
        while pos in snake or pos == apple:
            pos = (random.randint(0, width - 1), random.randint(0, height - 1))
        return pos

class SnakeGame:
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    def __init__(self):
        self.width = 8
        self.height = 16
        self.matrice = Matrice(23, width=self.width, height=self.height)
        self.joystick = Joystick(15, 2)       # 15 = X/2 = Y
        self.buzzer = Buzzer(21)              # 21 -> buzzer
        self.button = Pin(22, Pin.IN, Pin.PULL_UP)
        self.snake = [(4, 8)]
        self.direction = self.RIGHT
        self.apple = self.random_position()
        self.apple_count = 0
        self.applebeurks = [] 
        self.paused = False
        self.last_button_state = 1
        self.buzzer.play_start_sound()

    def random_position(self):
        return (random.randint(0, self.width - 1), random.randint(0, self.height - 1))

    def move_snake(self):
        new_head = (
            (self.snake[0][0] + self.direction[0]) % self.width,
            (self.snake[0][1] + self.direction[1]) % self.height
        )

        if new_head in self.snake:
            print("Collision = Game Over (self hit)")
            return False

        #zi on mange une pomme pourrie → game over
        for ab in self.applebeurks:
            if new_head == ab.position:
                print("AppleBeurk mangée = Game Over")
                return False

        self.snake.insert(0, new_head)

        if new_head == self.apple:
            self.apple_count += 1
            while self.apple in self.snake:
                self.apple = self.random_position()

            #spawn une pomme pourrie après chaque 2 pommes mange
            if self.apple_count % 2 == 0:
                self.applebeurks.append(AppleBeurk(self.snake, self.width, self.height, self.apple))

            #2e pomme pourrie après chaque 4 pommes mangées
            if self.apple_count % 4 == 0:
                self.applebeurks.append(AppleBeurk(self.snake, self.width, self.height, self.apple))

        else:
            self.snake.pop()

        return True

    def update_direction(self):
        x, y = self.joystick.read()
        new_direction = self.direction

        if x < 1000:
            new_direction = self.RIGHT
        elif x > 3000:
            new_direction = self.LEFT
        elif y > 3000:
            new_direction = self.UP
        elif y < 1000:
            new_direction = self.DOWN

        if (new_direction[0] != -self.direction[0] or new_direction[1] != -self.direction[1]):
            self.direction = new_direction

    def pause(self):
        current_state = self.button.value()
        if self.last_button_state == 1 and current_state == 0:
            self.paused = not self.paused
            print("Pause toggled:", self.paused)
            sleep(0.3)
        self.last_button_state = current_state

    def run(self):
        while True:
            self.pause()
            if self.paused:
                continue
            self.update_direction()
            if not self.move_snake():
                self.buzzer.play_game_over_sound()
                print("Game over")
                self.snake = [(4, 8)]
                self.direction = self.RIGHT
                self.apple = self.random_position()
                self.apple_count = 0
                self.applebeurks = []  #reinitialiser pommes pourrav
                sleep(1)
            self.matrice.update_display(self.snake, self.apple, self.applebeurks)
            sleep(0.3)

def run_snake():
    game = SnakeGame()
    game.run()

if __name__ == "__main__":
    run_snake()
