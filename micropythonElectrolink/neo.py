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

upperLimit = 1024
pwm0.freq(120)

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

def setTubeColor(n, hex):
    np[n] = hex_to_rgb(hex)

def setTubeColorAll(hex):
    t = hex_to_rgb(hex)
    for a in range(LEDS):
        np[a] = t
    np.write()

def writeColors():
    np.write()

def hex_to_rgb(value):
    """Return (red, green, blue) for the color given as #rrggbb."""
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def lerpColor(c1, c2, amt):
    """Return (red, green, blue) for two colors given as tuples and amt between 0.0 - 1.0"""
    if (amt < 0.0):
        amt = 0.0
    if (amt > 1.0):
        amt = 1.0

    r1 = c1[0]
    g1 = c1[1]
    b1 = c1[2]

    r2 = c2[0]
    g2 = c2[1]
    b2 = c2[2]

    r = int(r1 + (r2-r1)*amt)
    g = int(g1 + (g2-g1)*amt)
    b = int(b1 + (b2-b1)*amt)

    return (r,g,b)

def animateColors(tC, delay_ms, step=1):
    targetColor = hex_to_rgb(tC)
    for a in range(0, 101, step):
        t = a/100.0
        for i in range(LEDS):
            c = lerpColor(np[i], targetColor, t)
            np[i] = c
        np.write()
        sleep_ms(delay_ms)

def fadeinTube(delay_ms, color="#FFFFFF"):
    c = hex_to_rgb(color)
    for a in range(LED_MIDDLE+1):
        np[21-a] = c
        np[20+a] = c
        np.write()
        sleep_ms(delay_ms)

def fadeoutTube(delay_ms):
    for a in range(LED_MIDDLE+1):
        np[a] = (0, 0, 0)
        np[(LEDS-1)-a] = (0, 0, 0)
        np.write()
        sleep_ms(delay_ms)

fadeinTube(60)
fadeinLight(2)
fadeoutLight(3)
fadeoutTube(60)
