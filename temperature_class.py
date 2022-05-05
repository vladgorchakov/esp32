from machine import Pin
import time, onewire, ds18x20

class Sensor:
    def __init__(self, pin, num):
        self.__pin = pin
        self.__num = num
    
    def connect_to_line(self):
        ow = onewire.OneWire(Pin(self.__pin))
        self.__ds = ds18x20.DS18X20(ow)
        self.__roms = self.__ds.scan()
    
    def get_data(self):
        self.__ds.convert_temp()
        time.sleep(1)
        temp = self.__ds.read_temp(self.__roms[self.__num])
        return temp

temp = Sensor(12, 0)
temp.connect_to_line()
while True:
    print(temp.get_data())
    time.sleep(1)