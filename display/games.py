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

    def run(self):
        while True:
            if self.pin_right.value():
                if self.x < self.oled.width - 1:
                    self.x += 1
                else:
                    self.x = 0

            elif self.pin_down.value():
                if self.y < self.oled.height - 1:
                    self.y += 1
                else:
                    self.y = 0

            elif self.pin_left.value():
                if self.x > 0:
                    self.x -= 1
                else:
                    self.x = self.oled.width

            elif self.pin_up.value():
                if self.y > 0:
                    self.y -= 1
                else:
                    self.y = self.oled.height

            self.oled.pixel(self.x, self.y, 1)
            self.oled.show()
            sleep(0.01)

i2c = SoftI2C(scl=Pin(25), sda=Pin(26))
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

game = GraphicDisplayGame(oled, 12, 32, 18, 19)
game.run()
