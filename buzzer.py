# Bibliotheken laden
from machine import Pin, PWM
from time import sleep_ms

# PWM und GPIO initialisieren
pwm = PWM(Pin(16, Pin.OUT))

# 1. Parameter: Tastgrad (Duty Cycle)
pwm.duty_u16(30000)

# 2. Parameter: Frequenz in Hertz (Hz)
for freq in range (500, 2500, 100):
    print(freq, 'Hz')
    pwm.freq(freq)
    # Tondauer in Sekunden
    sleep_ms(500)

# PWM-Signal auf Dauer-Low (abschalten)
pwm.duty_u16(0)