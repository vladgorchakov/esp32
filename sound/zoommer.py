from time import sleep
from machine import Pin


class Zoommer:
    def __init__(self, pin, freq = 15):
        self.pin = Pin(pin, Pin.OUT)
        self.freq = freq
        self.period = 1/freq
        
    def sound(self, time):
        for i in range(int(time * self.freq)):
            self.pin.on()
            sleep(self.period/2)
            self.pin.off()
            sleep(self.period/2)
