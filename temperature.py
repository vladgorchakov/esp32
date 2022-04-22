from machine import Pin
import onewire
import time, ds18x20


ow = onewire.OneWire(Pin(12))
ds = ds18x20.DS18X20(ow)
roms = ds.scan()

while True:
    ds.convert_temp()
    time.sleep(3)
    print(ds.read_temp(roms[0]))
