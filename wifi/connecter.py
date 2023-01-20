import network
import ubinascii
from machine import Pin
from time import sleep


class WifiConnecter:
    def __init__(self, login: str, password: str) -> None:
        self.login = login
        self.__password = password
        self.__wlan = network.WLAN(network.STA_IF)
        self.__red_led = Pin(5, Pin.OUT)
        self.__yellow_led = Pin(19, Pin.OUT)
        self.__green_led = Pin(21, Pin.OUT)
    
    
    def check_connection(self) -> bool:
        counter = 0
        self.__yellow_led.on()
        print('\nconnection to:', self.login)
        while not self.__wlan.isconnected() and counter < 60:
            print('.', end='')
            counter += 1
            sleep(0.5)
        self.__yellow_led.off()
        print()
        
        return self.__wlan.isconnected()
        
        
    def connect(self) -> bool:
        self.__wlan.active(True)
        
        if not self.__wlan.isconnected():
            self.__wlan.connect(self.login, self.__password)
            return self.check_connection()
        else:
            print('(Connection already exists)\n')
            return True
        
        
    def get_info(self) -> dict:
        info = {
            'AP:': self.login,
            'MAC:': ubinascii.hexlify(network.WLAN().config('mac'),':').decode(),
            'IP:': self.__wlan.ifconfig()[0],
            'MASK:': self.__wlan.ifconfig()[1],
            'GATEWAY': self.__wlan.ifconfig()[2]
        }
        
        return info
    
    
    def run(self):
        if self.connect():
            self.__green_led.on()
            print('\n*Wifi connected*\n')
            for parm, info in self.get_info().items():
                print(parm, info, sep=':')
            print()
        else:
            print('Connection failed! Check your wifi router or login/password')
            self.__red_led.on()
