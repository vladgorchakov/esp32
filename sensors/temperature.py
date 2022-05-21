from machine import Pin
import time, onewire, ds18x20


class DsTempSensor:
    def __init__(self, pin):
        self.pin = pin
    
    
    def connect(self):
        ow = onewire.OneWire(Pin(self.pin))
        self.ds = ds18x20.DS18X20(ow)
        self.roms = self.ds.scan()
    
    
    def get_temp(self):
        self.ds.convert_temp()
        time.sleep(3)
        self.temp = self.ds.read_temp(self.roms[0])
        
        return self.temp

sensor = DsTempSensor(12)
sensor.connect()
