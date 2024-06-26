# from https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/5


from machine import Pin, Timer
from time import sleep

led = Pin(13, Pin.OUT)
timer = Timer()


def blink(timer):
    led.toggle()


timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)

# added this to end it
sleep(2)
timer.deinit()
led.off()