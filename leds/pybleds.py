import pyb
from time import sleep

class Leds:

    def __init__(self, delay=0.25):
        self.t = delay
        self.leds = [pyb.LED(i) for i in range(1, 5)]


    def blinking(self):
        leds = [pyb.LED(i) for i in range(1, 5)]

        for led in leds:
            led.on()
            sleep(self.t)

        for led in leds:
            led.off()
            sleep(self.t)
