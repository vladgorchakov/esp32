from machine import Pin
import onewire
import time, ds18x20


def weather_sens(temp):
    if temp < 17:
        return 'It is Cold!'
    elif temp > 21:
        return 'It is Hot!'
    else:
        return 'Is is normally!'

def main():
    ow = onewire.OneWire(Pin(12))
    ds = ds18x20.DS18X20(ow)
    roms = ds.scan()

    while True:
        ds.convert_temp()
        time.sleep(3)
        temp = ds.read_temp(roms[0])
        print(weather_sens(temp))
        
        
if __name__=="__main__":
    main()
