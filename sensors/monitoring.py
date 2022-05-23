import network
from umqtt.simple import MQTTClient
from machine import Pin, Timer
import time, onewire, ds18x20


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


def send_to_th(sensor_data):
    url = 'https://api.thingspeak.com/update?api_key=S5C0MUHLNFR9FOEY&field1='
    temp = str(get_temp(*sensor_data))
    print(temp)
    http_get(url + temp)
 

def send_to_nm(sensor_data):
    temp = str(get_temp(*sensor_data))
    print(temp)
    client = MQTTClient(client_id='7c:9e:bd:f4:c8:41', server='narodmon.ru', port=1883, user='vladislavzikstudy', password='k6tdd0pa')
    client.connect()    
    client.publish('dinartal/esp32/temperature', temp)
    

def start():
    sensor_data = connect_to_sensor(26)
    timer = Timer(0)
    timer.init(period=15000, mode=Timer.PERIODIC, callback=lambda t:send_to_th(sensor_data))
 
        
if __name__ == '__main__':
    start()
