import dht
import machine
import time

def read_dht(sensor):
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    return temp, hum

def main(pinio=27):
    pin = machine.Pin(pinio, Pin.IN, Pin.PULL_DOWN)
    sensor = dht.DHT22(pin)
    while True:
        time.sleep(2.0)
        t, h = read_dht(sensor)
        print('%.1f deg C\t%.1f humidity' % (t,h))

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        pinio = int(sys.argv[1])
        main(pinio)
    else:
        main()
