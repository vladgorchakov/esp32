from machine import Pin
import time, onewire, ds18x20


class TempSensor:
    def __init__(self, pin: int) -> None:
        self.pin = pin
        self.__ow = onewire.OneWire(Pin(self.pin))
        self.__ds = ds18x20.DS18X20(self.__ow)
        self.__roms = self.__ds.scan()
        self.__temp = 0
    
    
    @property
    def temp(self) -> float:
        try:
            self.__ds.convert_temp()
        except:
            print(f'No connected to temp sensor!')
            sleep(1)
            self.temp
        else:
            time.sleep(1)
            self.__temp = self.__ds.read_temp(self.__roms[0])
            return self.__temp
            

def main():
    sensor = TempSensor(25)
    print(sensor.temp)


if __name__=='__main__':
    main()
