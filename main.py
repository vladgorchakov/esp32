from clouds.thingspeak import Channel
from sensors.hudmitity import HudmSensor
from sensors.temperature import TempSensor
from time import sleep

pin_hs = 26
api_key = 'ZQT22H2MJ0E5QWYN'
pin_ts = 25

hs = HudmSensor(pin_hs)
ch = Channel(api_key)

hudm_id = 1
temp_id = 2
temp2_id = 3

ts = TempSensor(pin_ts)


while True:
    ch.add_field(hudm_id) #add first field to channel
    ch.add_field(temp_id) #add second field to channel
    ch.add_field(temp2_id) #add second field to channel
    
    if ch.write_field(hs.hudmitity, hudm_id):
        print('hudmitity sent')
    sleep(15)
    
    if ch.write_field(hs.temp, temp_id):
        print('temperature sent')
    sleep(15)
    
    if ch.write_field(ts.temp, temp2_id):
        print('temperature 2 sent')
    sleep(15)
