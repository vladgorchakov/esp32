from machine import Pin, SoftI2C
import ssd1306
from time import sleep

i2c = SoftI2C(sda=Pin(33), scl=Pin(32))
oled_width = 128
oled_height = 64
display = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)


ICON = [
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 1, 1, 0, 0, 0, 1, 1, 0],
    [ 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [ 0, 1, 1, 1, 1, 1, 1, 1, 0],
    [ 0, 0, 1, 1, 1, 1, 1, 0, 0],
    [ 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [ 0, 0, 0, 0, 1, 0, 0, 0, 0],
]

display.fill(0) # Clear the display
for i in range(0, 64, 55):
    for j in range(0, 128, 16):
        for y, row in enumerate(ICON):
            for x, c in enumerate(row):
                display.pixel(x + j, y + i, c)
        display.show()
        sleep(0.25)

display.text('Nelly,', 40, 15)
display.show()
display.text('I love you!', 20, 30)
display.show()

    
