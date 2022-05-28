import dht
import machine
import time


class HumSensor:
    def __init__(self, pin):
        self.pin = machine.Pin(pin)
        self.__hum = 0
        self.__temp = 0
        self.__sensor = dht.DHT11(self.pin)    
    
    
    @property
    def hudmitity(self):
        self.__sensor.measure()
        self.__hum = self.__sensor.humidity()
        return self.__hum
    
    
    @property
    def temp(self):
        self.__sensor.measure()
        self.__temp = self.__sensor.temperature()
        return self.__temp
    

hum = HumSensor(26)
print(hum.temp)
time.sleep(1)
print(hum.hudmitity)