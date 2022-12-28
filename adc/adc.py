from time import sleep


class ADC:
    def __init__(self, bit_depth, v_ref, pin):
        self.__adc_bit_depth = bit_depth
        self.__reference_voltage = v_ref
        self.__adc_levels = 2 ** self.__adc_bit_depth
        self.__one_level_value = self.__reference_voltage / self.__adc_levels
        self.__pin = pyb.ADC(pin)    
    
    def read_value(self):
        return self.__pin.read()
    
    def read_voltage(self):
        return self.read_value() * self.__one_level_value
    
    def get_sample_values(self, n, t):
        sample = []
        for i in range(n):
            sample.append(self.read_value())
            sleep(t)
            
        return sample
    
    def get_sample_voltage(self, n, t):
        sample = []
        for i in range(n):
            sample.append(self.read_voltage())
            sleep(t)
            
        return sample
    
    @property
    def adc_levels(self):
        return self.__adc_levels
    
    
    
class PotentiometerLedIndicator():
    def __init__(self, adc, leds: list):
        self.potentiometer = adc
        self.leds = leds
        self.total_intervals = len(leds)
        
        
    def get_intervals(self):
        values_interval = self.potentiometer.adc_levels / self.total_intervals
        inters = {}
        values = [i * values_interval for i in range(self.total_intervals + 1)]
        for i in range(1, self.total_intervals + 1):
            inters[i] = (values[i - 1], values[i])
        
        return inters
    
    
    def decode_val_to_interval(self, val, intervals):
        for interval_items in intervals.items():
            if val > interval_items[1][0] and val <= interval_items[1][1]:
                return interval_items[0]
    
    
    def indicate(self):
        intervals = self.get_intervals()
        interval = buf = 1
        current_leds = self.leds[0]
        while True:
            val = self.potentiometer.read_value()
            buf = self.decode_val_to_interval(val, intervals)
            if buf != interval and buf != None:
                current_leds.off()
                interval = buf
                current_leds = self.leds[interval - 1]
                current_leds.on()
                
            sleep(0.04)
    
    
    
def main():
    adc = ADC(12, 3, 'PA5')
    leds = [pyb.LED(i) for i in range(1, 5)]
    p = PotentiometerLedIndicator(adc, leds)
    p.indicate()
    
    
if __name__ == '__main__':
    main()
