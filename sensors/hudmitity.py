import dht
import machine
import time


class HudmSensor:
    def __init__(self, pin: int, name='Hudmitity', place='my room') -> None:
        self.name = name
        self.place = place
        self.pin = machine.Pin(pin)
        self.__hum = 0
        self.__temp = 0
        self.__sensor = dht.DHT11(self.pin)    
    
    
    @property
    def hudmitity(self) -> int:
        self.__sensor.measure()
        self.__hum = self.__sensor.humidity()
        
        return self.__hum
    
    
    @property
    def temp(self) -> int:
        self.__sensor.measure()
        self.__temp = self.__sensor.temperature()
        
        return self.__temp
    
    
    @property
    def hudmtemp(self) -> tuple:
        self.__sensor.measure()
        
        return self.__sensor.humidity(), self.__sensor.temperature()
    

def main() -> None:
    hudm = HudmSensor(26)
    print(f'*Sensor*\nName: {hudm.name}; Place: {hudm.place}')
    
    #1 using hudmitity and temp properties
    print(f'Temperature: {hudm.temp}')
    time.sleep(1)
    print(f'Hudmitity: {hudm.hudmitity}')
    time.sleep(1)
    
    #2 using hudmtemp property
    hudm_temp = hudm.hadmtemp
    print(f'Temperature: {hudm_temp[0]}')
    print(f'Hudmitity: {hudm_temp[1]}')


if __name__=='__main__':
    main()
