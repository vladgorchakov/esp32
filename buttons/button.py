import pyb


class Button:
    def __init__(self, pin_button: str):
        self.pin = pyb.Pin(pin_button, pyb.Pin.IN)
    self.irq_state = False


    def start_irq(self, handler_method):
        self.pin.irq(handler=handler_method, trigger=machine.Pin.IRQ_RISING)
