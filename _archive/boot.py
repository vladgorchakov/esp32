# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import webrepl
from wifi_connecter import do_router_connect


def main():
    try:
        login = 'IoT_339-1'
        password = '51048563'
        do_router_connect(login, password)
        webrepl.start()
    except:
        print('Not connected!')


if __name__ == '__main__':
    main()
