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
    

def main():
    adc = ADC(12, 3, 'PA5')
    print(adc.read_voltage())
    
if __name__ == '__main__':
    main()
