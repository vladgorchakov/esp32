import network
from time import sleep
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

while True:
    ap = sta_if.scan()
    #for i in range(len(ap)):
        #print(str(ap[i][0])[2:-1])
    print('___________')
    print('*total*: ' + str(len(ap)))
    print('___________')
    sleep(0.5)
