from machine import Pin
import time

# Define LED pin
led = Pin(18, Pin.OUT)   

while True:
    led.value(1)    # Led turns on
    sleep(1)    # Wait 1 second
    led.value(0)    # Led turns off
    sleep(1)    # Wait 1 second
