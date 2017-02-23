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

eyeCorrection = [  0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 
                    2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 
                    4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 
                    7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10, 11, 11, 
                    11, 12, 12, 12, 13, 13, 13, 14, 14, 15, 15, 15, 16, 16, 17, 17, 
                    17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24, 25, 
                    25, 26, 26, 27, 28, 28, 29, 29, 30, 31, 31, 32, 32, 33, 34, 34, 
                    35, 36, 37, 37, 38, 39, 39, 40, 41, 42, 43, 43, 44, 45, 46, 47, 
                    47, 48, 49, 50, 51, 52, 53, 54, 54, 55, 56, 57, 58, 59, 60, 61, 
                    62, 63, 64, 65, 66, 67, 68, 70, 71, 72, 73, 74, 75, 76, 77, 79, 
                    80, 81, 82, 83, 85, 86, 87, 88, 90, 91, 92, 94, 95, 96, 98, 99, 
                    100, 102, 103, 105, 106, 108, 109, 110, 112, 113, 115, 116, 118, 120, 121, 123, 
                    124, 126, 128, 129, 131, 132, 134, 136, 138, 139, 141, 143, 145, 146, 148, 150, 
                    152, 154, 155, 157, 159, 161, 163, 165, 167, 169, 171, 173, 175, 177, 179, 181, 
                    183, 185, 187, 189, 191, 193, 196, 198, 200, 202, 204, 207, 209, 211, 214, 216, 
                    218, 220, 223, 225, 228, 230, 232, 235, 237, 240, 242, 245, 247, 250, 252, 255]

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
    np[n] = eyeCorrection[hex_to_rgb(hex)]

def setTubeColorAll(hex):
    t = hex_to_rgb(hex)
    for a in range(LEDS):
        np[a] = eyeCorrection[t]
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
            np[i] = eyeCorrection[c]
        np.write()
        sleep_ms(delay_ms)

def fadeinTube(delay_ms, color="#FFFFFF"):
    c = hex_to_rgb(color)
    for a in range(LED_MIDDLE+1):
        np[21-a] = eyeCorrection[c]
        np[20+a] = eyeCorrection[c]
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
