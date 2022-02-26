import network


def do_connect(ssid, psw):
    ap = network.WLAN(network.AP_IF) # create access-point interface
    ap.config(essid=ssid, password=psw) # set the ESSID of the access point
    ap.config(max_clients=10) # set how many clients can connect to the network
    ap.active(True)         # activate the interface
    print(ap.ifconfig())
    
    

def main():
    ssid = "my-AP"
    psw = "51048563"
    do_connect(ssid, psw)
