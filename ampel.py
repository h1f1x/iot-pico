# First steps: https://www.elektronik-kompendium.de/sites/raspberry-pi/2612191.htm
# Blinking LEDs: https://www.elektronik-kompendium.de/sites/raspberry-pi/2612021.htm

from machine import Pin, PWM
from time import sleep

# Initialize GPIO pins for LEDs and Buzzer
led_green = Pin(13, Pin.OUT)
led_yellow = Pin(12, Pin.OUT)
led_red = Pin(11, Pin.OUT)
buz = PWM(Pin(16, Pin.OUT))
oled = Pin("LED", Pin.OUT)  # Onboard LED


def guard(func):
    """Decorator to wrap functionality with start indication and cleanup/stop."""

    def wrapper():
        def indicate_start():
            """Indicate the start of the process by blinking the onboard LED."""
            for _ in range(3):
                oled.on()
                sleep(0.5)
                oled.off()
                sleep(0.2)

        def all_off():
            """Turn off all outputs/devices."""
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
    """Operate the buzzer to indicate countdown and start."""
    buz.duty_u16(0)
    buz.freq(400)  # Set frequency to 400 Hz

    # Countdown beeps
    for _ in range(3):
        buz.duty_u16(20000)
        sleep(0.1)
        buz.duty_u16(0)
        sleep(1)

    # Final longer beep at higher frequency
    buz.freq(800)
    buz.duty_u16(15000)
    sleep(1.5)
    buz.duty_u16(0)


def init():
    """Initial setup to ensure a known state for all outputs/devices."""
    oled.on()
    led_red.off()
    led_green.off()
    led_yellow.off()
    buz.duty_u16(0)


@guard
def main():
    """Main function to execute the traffic light sequence."""
    init()
    led_red.on()
    buz_start_countdown()
    for _ in range(2):
        # Traffic light sequence
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
