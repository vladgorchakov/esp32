from machine import Pin, SoftI2C
import ssd1306
from time import sleep

class GraphicDisplayGame:
    def __init__(self, oled, pin_right, pin_down, pin_left, pin_up):
        self.oled = oled
        self.pin_right = Pin(pin_right, Pin.IN, Pin.PULL_DOWN)
        self.pin_down = Pin(pin_down, Pin.IN, Pin.PULL_DOWN)
        self.pin_left = Pin(pin_left, Pin.IN, Pin.PULL_DOWN)
        self.pin_up = Pin(pin_up, Pin.IN, Pin.PULL_DOWN)
        self.x = 0
        self.y = 0
        self.step_x = 3
        self.step_y = 2

    def draw_pixel(self):
        self.oled.pixel(self.x, self.y, 1)
        self.oled.show()

    def draw_rectangle(self, r_x, r_y):
        self.oled.fill(0)
        for y in range(self.y - r_y, self.y + r_y):
            for x in range(self.x - r_x, self.x + r_x):
                self.oled.pixel(x, y, 1)
        self.oled.show()

    def scan_position(self):
        while True:
            if self.pin_right.value():
                if self.x < self.oled.width - 1:
                    self.x += self.step_x
                else:
                    self.x = 0

            elif self.pin_down.value():
                if self.y < self.oled.height - 1:
                    self.y += self.step_y
                else:
                    self.y = 0

            elif self.pin_left.value():
                if self.x > 0:
                    self.x -= self.step_x
                else:
                    self.x = self.oled.width

            elif self.pin_up.value():
                if self.y > 0:
                    self.y -= self.step_y
                else:
                    self.y = self.oled.height

            return self.x, self.y


    def run(self):
        while True:
            self.scan_position()
            self.draw_rectangle(10, 10)
            sleep(0.01)


i2c = SoftI2C(scl=Pin(25), sda=Pin(26))
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

game = GraphicDisplayGame(oled, 12, 32, 18, 19)
game.run()
