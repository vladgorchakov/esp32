import machine


class LedIndicator:
    def __init__(self, name: str, pin: int) -> None:
        self.__red_pin = machine.Pin(pin)
    
    def display_hadm_state(self, hadm: int) -> None:
        if hadm > 60:
            self.__red_pin.on()
        else:
            self.__red_pin.off()
        
    def show_temp_state(self, temp: float) -> None:
        if temp > 30:
            self.__red_pin.on()
        else:
            self.__red_pin.off()
        