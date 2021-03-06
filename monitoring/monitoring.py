from clouds.thingspeak import Channel
from sensors.hudmitity import HudmSensor
from sensors.temperature import TempSensor
from time import sleep


class Sender:
    def __init__(self, api_key, pin_hs, pin_ts, hudm_id, temp_id, temp2_id):
        self.__hs = HudmSensor(pin_hs)
        self.__ts = TempSensor(pin_ts)
        self.__ch = Channel(api_key)
        self.hudm_fields = {hudm_id: self.__hs}
        self.temp_fields = {temp_id: self.__hs, temp2_id: self.__ts}
            
            
    def init_fields(self):
        for field in tuple(self.hudm_fields.keys()) + tuple(self.temp_fields.keys()):
            self.__ch.add_field(field)
    
    
    def send(self):
        sleep(1)
        for field, sensor in self.hudm_fields.items():
            self.__ch.write_field(sensor.hudmitity, field)
            print('hudm sent')
            sleep(15)
    
        for field, sensor in self.temp_fields.items():
            self.__ch.write_field(sensor.temp, field)
            print('temp' + str(field) + 'sent')
            sleep(15)
        
        
def main():    
    pass   
    
if __name__=='__main__':
    main()
