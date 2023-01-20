import socket
import gc
from machine import Pin
import json


class WebServer:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__indicator_pin = Pin(2, Pin.OUT)
        
    
    def get_json(self, temp_sensor, temp_log, humtemp_sensor, humtemp_log):
        data = {
            'ds18b20':
                {
                    'temperature_now': temp_sensor,
                    'log': temp_log
                },
            'dht11':
                {
                    'humidity_now': humtemp_sensor[0],
                    'temperature_now': humtemp_sensor[1],
                    'log': humtemp_log
                }
            }
        
        return json.dumps(data)
    

    def web_page(self, temp, hum):
        html = """<!DOCTYPE HTML><html><head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
        <style> html { font-family: times new roman; display: inline-block; margin: 0px auto; text-align: center; }
        h2 { font-size: 2.0rem; } p { font-size: 1.5rem; } .units { font-size: 1rem; } 
        .ds-labels{ font-size: 1.5rem; vertical-align:middle; padding-bottom: 15px; }
        </style></head><body><h2>BSUIR-IRT</h2><h3>1-339</h3>
        <p><i class="fas fa-thermometer-half" style="color:#059e8a;"></i> 
        <span class="ds-labels">Temperature (ds18b20):</span>
        <span id="temperature">""" + str(temp) + """</span>
        <sup class="units">&deg;C</sup>
        </p>
        <p><i class="fas fa-thermometer-half" style="color:#059e8a;"></i> 
        <span class="ds-labels">Humidity (DHT11):</span>
        <span id="temperature">""" + str(hum) + """</span>
        <sup class="units">%</sup>
        </p></body></html>"""
      
        return html


    def run(self, temp_sensor, hum_sensor):
        if gc.mem_free() < 102000:
                    gc.collect()
        
        self.s.bind(('', 80))
        self.s.listen(5)
        
        while True:
            try:
                conn, addr = self.s.accept()
                self.__indicator_pin.on()
                conn.settimeout(3.0)
                print('Connection: %s' % str(addr))
                request = conn.recv(1024)
                conn.settimeout(None)
                temp = temp_sensor.temp
                humtemp = hum_sensor.humtemp
                log_temp = temp_sensor.log
                print(log_temp)
                # response = self.web_page(temp, hum)
                # print(temp, hum)
                conn.send('HTTP/1.1 200 OK\n')
                conn.send('Content-Type: text/html\n')
                conn.send('Connection: close\n\n')
                # conn.sendall(self.web_page(temp, hum))
                conn.sendall(self.get_json(temp, temp_sensor.log, humtemp, hum_sensor.log))
                conn.close()
                self.__indicator_pin.off()
                
            except OSError as e:
                conn.close()
                self.__indicator_pin.off()
                print('Connection closed')
