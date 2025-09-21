from machine import Pin, ADC
from time import sleep

# Define pins
pot = ADC(Pin(32))            # Potentiometer connected to GPIO32 (ADC input)
pot.atten(ADC.ATTN_11DB)      # Full range: 0–3.3V (ESP32)
  # 12-bit resolution: 0–4095

while True:
    value = pot.read()            # Read potentiometer (0–4095)
    print("Pot: ", value)
    sleep(0.5)
