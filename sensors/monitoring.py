import network
from umqtt.simple import MQTTClient
from machine import Pin
import time, onewire, ds18x20
from machine import Timer


def http_get(url):
    import socket
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))    
    s.close()


def connect_to_sensor(pin):
    ow = onewire.OneWire(Pin(26))
    ds = ds18x20.DS18X20(ow)
    roms = ds.scan()    
    return ds, roms


def get_temp(ds, roms):
    ds.convert_temp()
    time.sleep(3)

    return ds.read_temp(roms[0])

def send_temp(temp):
    url = 'https://api.thingspeak.com/update?api_key=S5C0MUHLNFR9FOEY&field1='
    temp = str(temp)
    #client = MQTTClient(client_id='7c:9e:bd:f4:c8:41', server='narodmon.ru', port=1883, user='vladislavzikstudy', password='k6tdd0pa')
    #client.connect()    
    #client.publish('dinartal/esp8266/temperature', temp)
    http_get(url + temp)
 
def start():
    while True:
        temp = get_temp(*connect_to_sensor(26))
        send_temp(temp)
        print(temp)
        time.sleep(15)        
    
def main():
    pass
        
if __name__ == '__main__':
    start()
