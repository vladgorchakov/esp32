import pyb
from time import sleep


class ButtonLedBlinking:
    def __init__(self):
        self.leds = Leds()
        self.button = Button('PA0')
        self.led_blinking_state = False

    def irq_handler(self, pin):
        if not self.led_blinking_state:
            self.led_blinking_state = True
            self.leds.blinking()
            self.led_blinking_state = False

    def start(self):
        self.button.start_irq(self.irq_handler)

if __name__ == '__main__':
    blb = ButtonLedBlinking()
    blb.start()
