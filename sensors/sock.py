import socket

url = "https://api.thingspeak.com/update?api_key=ZQT22H2MJ0E5QWYN&field1=38"

#api
host = "api.thingspeak.com"
path = "update?api_key=ZQT22H2MJ0E5QWYN&field1=38"
addr = socket.getaddrinfo(host, 80)[0][-1]
s = socket.socket()
s.connect(addr)
s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))

while True:
    data = s.recv(1000)
    if data:
        print(str(data, 'utf8')[len(data) - 2: len(data)], end='')
    else:
        break

s.close()