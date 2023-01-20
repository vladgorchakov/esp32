import socket


class Channel:
    def __init__(self, api_key: str) -> None:
        self.__host = "api.thingspeak.com"
        self.__api_key = api_key
        self.__channel_path = "update?api_key=" + api_key + '&' + 'field'
        self.__fields = {} #channels

    def add_field(self, field_id: int, name: str):
        field_path = self.__channel_path + str(field_id) + '='
        self.__fields[field_id] = Field(field_id, field_path, name=name) #create new Field and and to dict

    @property
    def fields(self):
        return self.__fields

    def write_field(self, data: float, field_id: int) -> None:
        addr = socket.getaddrinfo(self.__host, 80)[0][-1]
        return self.__fields[field_id].write(self.__host, addr, data)


class Field:
    def __init__(self, field_id, path: str, name='') -> None:
        self.__id = field_id
        self.name = name
        self.__value = 0
        self.__field_path = path
        
    @staticmethod
    def check_sending(data) -> bool:
        try:
            num_get = int(str(data, 'utf8').split('\n')[-1])
        except:
            print('Not integer value')
            return False
        else:
            if num_get != 0:
                return num_get
            else:
                return False
            

    def write(self, host, addr, value) -> bool:
        try:
            path = self.__field_path + str(value)
            s = socket.socket()
            s.connect(addr)
            s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
            data = s.recv(1000)
            s.close()

            if self.check_sending(data):
                self.__value = value
                return True
            else:
                return False
        except:
            return False

    @property
    def value(self):
        return self.__value


def main():
    pass
        
        
if __name__=='__main__':
    main()
