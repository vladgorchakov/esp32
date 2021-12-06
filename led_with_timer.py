from machine import Timer, Pin, freq

def led_blink(led):
    if led.value() == 1:
        led.off()
    else:
        led.on()
        
led25 = Pin(25, Pin.OUT)
timer = Timer(0)
timer.init(period=1000, mode=Timer.PERIODIC, callback=lambda func:led_blink(led25))

led33 = Pin(33, Pin.OUT)
timer1 = Timer(1)
timer1.init(period=250, mode=Timer.PERIODIC, callback=lambda func:led_blink(led33))
