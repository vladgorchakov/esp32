import socket

url = "https://api.thingspeak.com/update?api_key=ZQT22H2MJ0E5QWYN&field1=38"

_, _, host, path = url.split('/', 3)
addr = socket.getaddrinfo(host, 80)[0][-1]
s = socket.socket()
s.connect(addr)
b = bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8')

# while True:
#     data = s.recv(100)
#     if data:
#         print(str(data, 'utf8'), end='')
#     else:
#         break
# s.close()


#