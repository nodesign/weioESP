import lightDouble
from machine import Pin, I2C, unique_id
import vl6180
import time
import ubinascii
from umqtt.simple import MQTTClient
from ujson import loads, dumps
import network

ms_delay = 3
upper = 110
lower = 20

server="78.194.220.232"
CLIENT_ID = ubinascii.hexlify(unique_id())
REQUEST_TOPIC = b"weio_command"
ANSWER_TOPIC = b"weio_reply"
ERROR_TOPIC = b"weio_error"

debugLed = Pin(2, Pin.OUT)

def proportion(value, istart, istop, ostart, ostop):
    return float(ostart) + (float(ostop) - float(ostart)) * ((float(value) - float(istart)) / (float(istop) - float(istart)))

# Received messages from subscriptions will be delivered to this callback
def sub_cb(topic, msg):
    global c
    global lamp

    data = loads(msg)
    method = data["method"]
    params = data["params"]
    #print(params)
#PERCENT
    lamp.setMixPercent(params[0])


# construct an I2C bus fro VL6180 sensor
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
proxy = vl6180.Sensor(i2c)
time.sleep_ms(500)

pinWarm = Pin(12, Pin.OUT)
pinCold = Pin(14, Pin.OUT)

lamp = lightDouble.Lamp(pinWarm, pinCold)

c = None

# wait to connect to the network
print("waiting to be connected")
sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
while not(sta_if.isconnected()):
    debugLed.value(1)
    time.sleep(0.1)
    debugLed.value(0)
    time.sleep(0.1)

print("connected to the network")
print(sta_if.ifconfig())

c = MQTTClient(CLIENT_ID, server)
c.set_callback(sub_cb)
c.connect()
c.subscribe(REQUEST_TOPIC)
print("entering loop")


while True :
    val = proxy.range()
    #print(val)
    delta = 0
    if (val < upper):
        if (val > upper):
            val = upper
        if (val < lower):
            val = lower

        l = int(proportion(val, lower, upper, 0,255))

        delta = ms_delay * abs(l- lamp.getLight())
        lamp.fade(l,ms_delay)

    if ((delta > 0) and (delta < 150)):
        time.sleep_ms(150-delta)
    else :
        time.sleep_ms(150)
    c.check_msg()
