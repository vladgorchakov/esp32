# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import webrepl
from wifi.connecter import WifiConnecter
from monitoring.monitoring import Sender
from time import sleep


def connect_to_network(login, password):
    wifi = WifiConnecter(login, password)
    
    if wifi.connect():
        print('\n*Wifi connected*\n')
        for parm, info in wifi.get_info().items():
            print(parm, info, sep=':')
        print()
        
        webrepl.start()
    else:
        print('Connection failed! Check your wifi router or login/password')    


def main():
    login = ''
    password = ''
    api_key = ''
    
    connect_to_network(login, password)
    
    mon = Sender(api_key, 26, 25, 1, 2, 3)
    mon.init_fields()
    while True:
        mon.send()
        
        
if __name__ == '__main__':
    pass
    main()
