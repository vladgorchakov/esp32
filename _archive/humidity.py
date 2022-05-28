import dht
import machine
from time import sleep



def switch_led(h):
    if h > 60:
        pin32.on()
    else:
        pin32.off()
        
    

pin26 = machine.Pin(26)
pin32 = machine.Pin(32, machine.Pin.OUT)
d = dht.DHT11(pin26)



while True:
    print(d.measure())
    print(d.temperature())
    hum = d.humidity()
    switch_led(hum)
    print(hum)
    sleep(2)

    