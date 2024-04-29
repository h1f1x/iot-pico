# See: https://github.com/RaspberryPiFoundation/picozero/tree/main

from picozero import pico_led, Button
from time import sleep

button = Button(10)

pico_led.blink()

