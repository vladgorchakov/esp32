import machine


class LedIndicator:
    def __init__(self, name: str, pin1: int, pin2: int, pin3: int) -> None:
        self.__red_pin = machine.Pin(pin1)
        self.__green_pin = machine.Pin(pin2)
        self.__blue_pin = machine.Pin(pin3)
    
    
    def display_hadm_state(self, start_value, end_value, current_value) -> None:
        if current_value > end_value:
            self.__red_pin.on()
            self.__blue_pin.off()
            self.__green_pin.off()
            
        elif current_value < start_value:
            self.__blue_pin.on()
            self.__red_pin.off()
            self.__green_pin.off()
        
        else:
            self.__green_pin.on()
            self.__blue_pin.off()
            self.__red_pin.off()