# This should run automatically
from machine import Pin, PWM
from time import sleep

oled = Pin("LED", Pin.OUT)  # Onboard LED

led = Pin(13, Pin.OUT)
onboard_led = Pin("LED", Pin.OUT)

# PIN 36 3V Out connected to the button
# GP 10 to the button
button = Pin(10, Pin.IN, Pin.PULL_DOWN)

onboard_led.on()
pressed_count = 0

while True:
    if button.value():
        led.toggle()
        sleep(0.5)
        pressed_count += 1
        # Test for long press of the button
        if pressed_count > 4:
            break
    else:
        pressed_count = 0

# shutdown
led.off()
onboard_led.off()
