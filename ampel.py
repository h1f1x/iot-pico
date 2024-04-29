# Bibliotheken laden
from machine import Pin, PWM
from time import sleep

led_green = Pin(13, Pin.OUT)
led_yellow = Pin(12, Pin.OUT)
led_red = Pin(11, Pin.OUT)
oled = Pin("LED", Pin.OUT)
buz = PWM(Pin(16, Pin.OUT))

def guard(func):
    def wrapper():
        def indicate_start():
            for i in range(3):
                oled.on()
                sleep(0.5)
                oled.off()
                sleep(0.2)

        def all_off():
            buz.duty_u16(0)
            oled.off()
            led_red.off()
            led_green.off()
            led_yellow.off()
        
        all_off()
        indicate_start()
        func()
        all_off()

    return wrapper

def buz_start_countdown():
    buz.duty_u16(0)

    # PWM-Einstellung: Frequenz in Hertz (Hz)
    buz.freq(400)

    for i in range(3):
        buz.duty_u16(20000)
        sleep(0.1)
        buz.duty_u16(0)
        sleep(1)

    
    buz.freq(800)
    buz.duty_u16(15000)
    sleep(1.5)
    buz.duty_u16(0)

def init():
    oled.on()
    led_red.off()
    led_green.off()
    led_yellow.off()
    buz.duty_u16(0)

    
@guard
def main():
    init()
    led_red.on()
    buz_start_countdown()
    for i in range(2):
        # LED einschalten
        led_yellow.on()
        sleep(1)
        led_red.off()
        led_yellow.off()
        led_green.on()
        sleep(3)
        led_green.off()
        led_yellow.on()
        sleep(2)
        led_yellow.off()
        led_red.on()
        sleep(2)

main()