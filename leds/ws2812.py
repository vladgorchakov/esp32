from machine import Pin
from neopixel import NeoPixel
from time import sleep
from random import randint


class PixelLeds:
    def __init__(self, leds_count=8, leds_pin=14):
        self.n = leds_count
        self.pin = Pin(leds_pin, Pin.OUT)
        self.np = NeoPixel(self.pin, self.n)
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)

    def gen_any_color(self):
        return (randint(0, 255), randint(0, 255), randint(0, 255))

    def clear(self):
        for i in range(self.n):
            self.np[i] = (0, 0, 0)
        self.np.write()

    def make_white(self):
        for i in range(self.n):
            self.np[i] = (255, 255, 255)
        self.np.write()

    def write_leds(self, color, start=0, step=1, delay=0):
        for i in range(start, self.n, step):
            self.np[i] = color
            sleep(delay)
            self.np.write()

    def write_leds_reverse(self, color, stop=-1, step=-1, delay=0):
        for i in range(self.n - 1, stop, step):
            self.np[i] = color
            sleep(delay)
            self.np.write()

    def play_colors(self, colors, delay, pause=0):
        for color in colors:
            self.write_leds(color, delay=pause)
            sleep(delay)

    def play_any_colors(self, delay, pause=0):
        while True:
            color = self.gen_any_color()
            self.write_leds(color, delay=pause, step=2)
            sleep(delay)

    def play_any_colors_reverse(self, delay, pause=0):
        while True:
            color = self.gen_any_color()
            self.write_leds_reverse(color, delay=pause)
            sleep(delay)

    def play_any_colors_all(self, delay, pause=0):
        while True:
            color = self.gen_any_color()
            self.write_leds_reverse(color, delay=pause, step=-2)
            sleep(delay)
            color = self.gen_any_color()
            self.write_leds(color, delay=pause, start=0, step=2)
            sleep(delay)

def main():
    leds = PixelLeds(8, 14)
    leds.make_white()
    while True:
        leds.play_any_colors_all(0.05, 0.05)


if __name__ == '__main__':
    main()
