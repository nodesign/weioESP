from machine import Pin, PWM
from neopixel import NeoPixel
from time import sleep, sleep_ms

# NEOPIXEL output pin
pin = Pin(5, Pin.OUT, Pin.PULL_UP)

# Total of 42 LEDs
LEDS = 42
LED_MIDDLE = 21
np = NeoPixel(pin, LEDS)

for i in range(LEDS):
    np[i] = (0,0,0)
    np.write()

# PWM PIN
pwm0 = PWM(Pin(4))

upperLimit = 255
pwm0.freq(upperLimit)

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

def setTubeColor(n, r,g,b):
    np[n] = (r,g,b)

def writeColors():
    np.write()


# while True :
#     for a in range(LED_MIDDLE+1):
#         currA = 21-a
#         currB = 20+a
# #        np[currA] = (255, 115, 20)
# #        np[currB] = (255, 115, 20)
#         np[currA] = (255, 115, 20)
#         np[currB] = (255, 115, 20)
#
#         #print(currA, currB)
#         np.write()
#         sleep_ms(50)
#
#     fadeinLight()
#     fadeoutLight()
#
#     for a in range(LED_MIDDLE+1):
#         np[a] = (0, 0, 0)
#         np[(LEDS-1)-a] = (0, 0, 0)
#
#         np.write()
#         sleep_ms(50)
#
#     fadeinLight()
#     fadeoutLight()
