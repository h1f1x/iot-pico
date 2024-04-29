# from https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/6

from machine import Pin
import time

led = Pin(13, Pin.OUT)

# PIN 36 3V Out connected to the button
# GP 10 to the button
button = Pin(10, Pin.IN, Pin.PULL_DOWN)

while True:
    if button.value():
        led.toggle()
        time.sleep(0.5)
