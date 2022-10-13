from machine import Pin, SoftI2C
import ssd1306
from time import sleep

i2c = SoftI2C(scl=Pin(25), sda=Pin(26))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
oled.fill(0)


x = 0
y = 0
oled.pixel(x, y, 1)
oled.show()

pin_right = Pin(12, Pin.IN, Pin.PULL_DOWN)
pin_down = Pin(32, Pin.IN, Pin.PULL_DOWN)
pin_left = Pin(18, Pin.IN, Pin.PULL_DOWN)
pin_up = Pin(19, Pin.IN, Pin.PULL_DOWN)

while True:
    if pin_right.value():
        if x < oled_width:
            x += 1
        else:
            x = 0

    elif pin_down.value():
        if y < oled_height:
            y += 1
        else:
            y = 0

    elif pin_left.value():
        if x > 0:
            x -= 1
        else:
            x = oled_width

    elif pin_up.value():
        if y > 0:
            y -= 1
        else:
            y = oled_height

    oled.pixel(x, y, 1)
    oled.show()
    sleep(0.01)
