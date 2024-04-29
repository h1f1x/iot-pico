# Bibliotheken laden
from machine import Pin
from time import sleep

def status_led():
    def wrapper():
        oled = Pin("LED", Pin.OUT)
        for i in range(3):
            oled.on()
            sleep(0.5)
            oled.off()
            sleep(0.2)
        func()
        oled.off()
    return wrapper
