from machine import Pin, PWM
from time import sleep, sleep_ms

# switch protections
def up():
    if (pin_int.value()):
        pinA.value(1)
        pinB.value(0)

def down():
    if (pin_int.value()):
        pinA.value(0)
        pinB.value(1)

def stop(pin=None):
    pinA.value(0)
    pinB.value(0)
    print("stop")

def fadeinLight(delay_ms):
    for a in range(upperLimit):
        pwm0.duty(a)
        sleep_ms(delay_ms)
    pwm0.duty(upperLimit)

def fadeoutLight(delay_ms):
    for a in range(upperLimit):
        pwm0.duty(upperLimit-a)
        sleep_ms(delay_ms)
    pwm0.duty(0)

def lighting(value):
    pwm0.duty(value)

# motor control
pinA = Pin(14, Pin.OUT)
pinB = Pin(12, Pin.OUT)

# Security switch
pin_int = Pin(13, Pin.IN, Pin.PULL_UP)
pin_int.irq(trigger=Pin.IRQ_FALLING, handler=stop)

# light control
# PWM PIN
pwm0 = PWM(Pin(5))

upperLimit = 1024
pwm0.freq(120)


stop()
