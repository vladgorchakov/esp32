from machine import Timer
timer = Timer(0)
timer.init(period=1000, mode=Timer.PERIODIC, callback=lambda t:print('Hello'))
