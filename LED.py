from machine import Pin
import time

# Define LED pin
led = Pin(18, Pin.OUT)   

while True:
    led.on()          # LED ON
    time.sleep(1)     # Wait 1 second
    led.off()         # LED OFF
    time.sleep(1)     # Wait 1 second
