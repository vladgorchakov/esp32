from machine import Pin, SoftI2C
import ssd1306
from time import sleep
from random import randint
from math import sin, cos, radians

class Graph:
    def __init__(self, oled):
        self.oled = oled


    def draw_graph(self, oled):
        for y in range(oled.height):
            pirnt(y)

    def draw_sin(self, start=0, stop=7200, step=7):
        x_s = 0
        for x in range(start, stop, step):
            y = self.oled.height/2 + self.oled.height/2 * sin(radians(x))
            if x_s > self.oled.width:
                x_s = 0
                self.oled.fill(0)
            self.oled.pixel(x_s, int(y), 1)
            self.oled.show()
            x_s += 1

    def make_noise(self):
        while True:
            self.oled.fill(0)
            for y in range(0, self.oled.height, 2):
                for x in range(0, self.oled.width, 2):
                    self.oled.pixel(x + randint(0, 5), y + randint(0, 5), 1)
            self.oled.show()


def main():
    i2c = SoftI2C(scl=Pin(25), sda=Pin(26))

    oled_width = 128
    oled_height = 64
    oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

    gr = Graph(oled)
    gr.draw_sin()

if __name__ == '__main__':
    main()
