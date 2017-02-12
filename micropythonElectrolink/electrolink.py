from machine import Pin, PWM

# 16 GPIO of ESP board
pins = [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None]

# list of function capability
#capability = ["numberOfPins":len(pins), "pinModes":["IN", "OUT", "PULL_UP"],"interfaces":["UART", "SPI", "PWM", "I2C"], "functions":["pwmStart", "pwmSet", "pwmStop", "pinMode", "digitalWrite", "digitalRead"]]

# PWM
def pwmStart(pwmNb, frequence):
    pwm = PWM(Pin(pwmNb))
    pwm.freq(frequence)
    pins[pwmNb] = pwm

def pwmSet(pwmNb, duty):
    pins[pwmNb].duty(duty)

def pwmStop(pwmNb):
    pins[pwmNb].deinit()
    pins[pwmNb] = None

# digital GPIO
def pinMode(pinId, mode):
    gpio = None
    if (mode is 0):
        mode = Pin.OUT
        gpio = Pin(pinId, mode)
    elif(mode is 1):
        mode = Pin.IN
        gpio = Pin(pinId, mode)
    elif(mode is 2):
        mode = Pin.PULL_UP
        gpio = Pin(pinId, Pin.IN, Pin.PULL_UP)
    else:
        print("Mode not supported in hardware")
    pins[pinId] = gpio

def digitalWrite(pinId, value):
    pins[pinId].value(value)

def digitalRead(pinId):
    return pins[pinId].value()
