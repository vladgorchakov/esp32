import webrepl


def do_connect(login, password):
    import network
    from time import sleep
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network:')
        wlan.connect(login, password)
        while not wlan.isconnected():
            print('.', end='')
            sleep(0.5)
    print('\nnetwork config:', wlan.ifconfig())
    
    
def main():
    login = 'MTS_111'
    password = '35139812'
    do_connect(login, password)
    webrepl.start()

if __name__ == "__main__":
    main()