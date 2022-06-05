import dht
import machine
import time


class HudmSensor:
    def __init__(self, pin: int, name='hudmitity', place='my room') -> None:
        self.name = name
        self.place = place
        self.pin = machine.Pin(pin)
        self.__hum = 0
        self.__temp = 0
        self.__sensor = dht.DHT11(self.pin)    
    
    
    @property
    def hudmitity(self) -> int:
        while True:
            try:
                print('checking')
                self.__sensor.measure()
                self.__hum = self.__sensor.humidity()            
                return self.__hum
            except:
                print('ERROR of updating value from .measure()')
                time.sleep(2)
                
                
    
    @property
    def temp(self) -> int:
        while True:
            try:
                self.__sensor.measure()
                self.__temp = self.__sensor.temperature()
                return self.__temp 
            except:
                print('ERROR of updating value from .measure()')
                time.sleep(2)
                
    
    @property
    def hudmtemp(self) -> tuple:
        while True:
            try:
                self.__sensor.measure()
                return self.__sensor.humidity(), self.__sensor.temperature()
            except:
                print('ERROR of updating value from .measure()')
                time.sleep(2)
    

def main() -> None:
    hudm = HudmSensor(26)
    print(f'*Sensor*\nName: {hudm.name}; Place: {hudm.place}')
    
    #1 using hudmitity and temp properties
    print(f'Temperature: {hudm.temp}')
    time.sleep(1)
    print(f'Hudmitity: {hudm.hudmitity}')
    time.sleep(1)
    
    #2 using hudmtemp propertyss
    hudm_temp = hudm.hudmtemp
    print(f'Temperature: {hudm_temp[0]}')
    print(f'Hudmitity: {hudm_temp[1]}')


if __name__=='__main__':
    main()
