import network


def do_router_connect(login, password):
    from time import sleep
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network:')
        counter = 0
        wlan.connect(login, password)
        while not wlan.isconnected() and counter < 60:
            print('*', end='')
            counter += 1
            sleep(0.5)
    print('\nyour router:', login)
    print('network config:', wlan.ifconfig())
    

def do_ap_connect(ssid='MyEspAP', psw='11111111'):
    ap = network.WLAN(network.AP_IF) # create access-point interface
    ap.config(essid=ssid, password=psw) # set the ESSID of the access point
    ap.config(max_clients=10) # set how many clients can connect to the network
    ap.active(True)         # activate the interface
    print('ssid: ' + ssid)
    print('password: ' + psw)
    print(ap.ifconfig())
