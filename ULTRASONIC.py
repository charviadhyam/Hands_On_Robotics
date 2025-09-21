from machine import Pin, time_pulse_us
from time import sleep 

trig = Pin(33, Pin.OUT)
echo = Pin(35, Pin.IN)

def get_distance():
    trig.value(0)
    sleep(1)
    trig.value(1)
    sleep(1)
    trig.value(0)

    duration = time_pulse_us(echo, 1, 30000)  
    distance = (duration / 2) / 29.1
    return distance

while True:
        d = get_distance()
        print("Distance ",d,' cm')
sleep(1)
