import socket


class ThingSpeak:
    def __init__(self, api_key: str) -> None:
        self.__host = "api.thingspeak.com"
        self.__api_key = "ZQT22H2MJ0E5QWYN"
        self.__path = "update?api_key=" + api_key + '&' + 'field'
    
    
    def write(self, data: float, field: int) -> None:
        path = self.__path + str(field) + '=' + str(data)
        addr = socket.getaddrinfo(self.__host, 80)[0][-1]
        s = socket.socket()
        s.connect(addr)
        s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, self.__host), 'utf8'))
        s.close()
