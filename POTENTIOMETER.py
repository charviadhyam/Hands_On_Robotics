from machine import Pin, ADC, PWM
import time

# Define pins
pot = ADC(Pin(34))            # Potentiometer connected to GPIO34 (ADC input)
pot.atten(ADC.ATTN_11DB)      # Full range: 0–3.3V (ESP32)
pot.width(ADC.WIDTH_12BIT)    # 12-bit resolution: 0–4095

while True:
    pot_value = pot.read()            # Read potentiometer (0–4095)
    print("Pot:", pot_value)
    time.sleep(0.05)
