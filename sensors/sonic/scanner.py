from .sonic import HCSR04
from time import sleep
from machine import Pin, SoftI2C
import ssd1306
from zoommer import Zoommer


class SonicScanner:
    def __init__(self, sensor, oled, zoommer):
        self.sensor = sensor
        self.oled = oled
        self.zoommer = zoommer
    
    def send_to_display(self, distance):
        self.oled.fill(0)
        self.oled.text('DISTANCE: ', 0, 0)
        self.oled.text(str(distance) + ' cm', 0, 20)
        self.oled.show()
        
    def check_distance(self, distance):
        if distance > 10 and distance < 50:
            self.zoommer.sound(1)
            
    def start(self):
        while True:
            distance = self.sensor.distance_cm()
            self.send_to_display(distance)
            self.check_distance(distance)



def main():
    i2c = SoftI2C(scl=Pin(25), sda=Pin(26))
    oled_width = 128
    oled_height = 64
    oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
    sensor = HCSR04(trigger_pin=16, echo_pin=17, echo_timeout_us=10000)
    z = Zoommer(18, 25)
    scan = SonicScanner(sensor, oled, z)
    scan.start()


if __name__ == '__main__':
    main()
 