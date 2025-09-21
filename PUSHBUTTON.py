from machine import Pin
from time import sleep

button = Pin(21, Pin.IN, Pin.PULL_UP)   # Button pin with pull-down resistor
led = Pin(22, Pin.OUT)                    # LED pin

while True:
    if button.value() == 0:   # Button pressed
        led.value(1)
    else:                     # Button not pressed
        led.value(0)
    sleep(1)          # Small delay for stability
