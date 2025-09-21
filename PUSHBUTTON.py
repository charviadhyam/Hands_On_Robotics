from machine import Pin
from time import sleep

button = Pin(14, Pin.IN, Pin.PULL_DOWN)   # Button pin with pull-down resistor
led = Pin(5, Pin.OUT)                    # LED pin

while True:
    if button.value() == 0:   # Button pressed
        led.value(1)
    else:                     # Button not pressed
        led.value(0)
    sleep(1)          # Small delay for stability
