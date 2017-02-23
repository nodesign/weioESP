from machine import PWM
from time import sleep_ms
from math import exp

class Lamp:
    def __init__(self, pin):
        self.pwm0 = PWM(pin)
        self.upperLimit = 1023
        self.pwm0.freq(120)
        self.fader = [	0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 
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
        self.current = 0 # 0-255

    def getLight(self):
        return self.current

    def fadeinLight(self, delay_ms):
        for a in range(256):
            self.lighting(a)
            sleep_ms(delay_ms)

    def fadeoutLight(self, delay_ms):
        for a in range(256):
            self.lighting(255-a)
            sleep_ms(delay_ms)

    def fade(self, val, delay_ms):
        delta = abs(val - self.current)
        if (val > self.current):
            for a in range(delta):
                self.lighting(self.current+1)
                sleep_ms(delay_ms)

        elif (val < self.current):
            for a in range(delta):
                self.lighting(self.current-1)
                sleep_ms(delay_ms)

    def lighting(self, value):
        self.pwmOutput(self.fader[value]) # apply correction for humain eyes
        self.current = value

    def pwmOutput(self, val):
        """Convert from 0-255 to 0-1023 and send to PWM driver"""
        self.pwm0.duty(round(val*4.011))

    def sfunction(self, t):
        """Function to calculate S function curve. Input 0-255 output 0-255"""
        return int(1.0/(1.0+exp(((t/21.0)-6.0)*-1.0))*255)