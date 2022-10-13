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

pin_x = Pin(12, Pin.IN, Pin.PULL_DOWN)
pin_y = Pin(32, Pin.IN, Pin.PULL_DOWN)

while True:
    print(pin_x.value(), pin_y.value())
    if pin_x.value():
        if x < oled_width:
            x += 1
        else:
            x = 0
        oled.pixel(x, y, 1)
    elif pin_y.value():
        if y < oled_height:
            y += 1
        else:
            y = 0
        oled.pixel(x, y, 1)
    oled.show()
    sleep(0.01)
