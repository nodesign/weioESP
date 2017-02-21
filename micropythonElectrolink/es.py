import time
import ubinascii
from umqtt.simple import MQTTClient
from ujson import loads, dumps
import electrolink
import machine
import network
import neo

server="78.194.220.232"
CLIENT_ID = ubinascii.hexlify(machine.unique_id())
REQUEST_TOPIC = b"weio_command"
ANSWER_TOPIC = b"weio_reply"
ERROR_TOPIC = b"weio_error"
c = None

# Received messages from subscriptions will be delivered to this callback
def sub_cb(topic, msg):
    global c
    #print((topic, msg))

# There is no need to check topic as there will be only one subscription
#    if (topic == REQUEST_TOPIC):

    data = loads(msg)
    method = data["method"]
    params = data["params"]
    #print(params)
#PWM
    if   (method is "pwmStart"):
        electrolink.pwmStart(params[0], params[1])
    elif (method is "pwmSet"):
        electrolink.pwmSet(params[0], params[1])
    elif (method is "pwmStop"):
        electrolink.pwmStop(params[0])
#DIGITAL GPIO
    elif (method is "pinMode"):
        electrolink.pinMode(params[0], params[1])
    elif (method is "digitalWrite"):
        electrolink.digitalWrite(params[0], params[1])
    elif (method is "digitalRead"):
        value = electrolink.digitalRead(params[0])
        p = {"requested":"digitalRead", "value":[params[0],params[1],value]} #pass back pinId to client
        out = dumps(p)
        c.publish(ANSWER_TOPIC, out)

# LAMP
    elif (method is "fadeIn"):
        neo.fadeinLight()
    elif (method is "fadeOut"):
        neo.fadeoutLight()
    elif (method is "lighting"):
        neo.lighting(params[0])
    elif (method is "setTubeColor"):
        neo.setTubeColor(params[0], params[1])
    elif (method is "writeColors"):
        neo.writeColors()
    elif (method is "setTubeColorAll"):
        neo.setTubeColorAll(params[0])
    elif (method is "animateColors"):
        neo.animateColors(params[0], params[1], params[2])
    elif (method is "fadeinTube"):
        neo.fadeinTube(params[0], params[1])
    elif (method is "fadeoutTube"):
        neo.fadeoutTube(params[0])

def start():
    # wait to connect to the network
    print("waiting to be connected")
    sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
    while not(sta_if.isconnected()):
        time.sleep(0.3)
    print("connected to the network")
    print(sta_if.ifconfig())

    c = MQTTClient(CLIENT_ID, server)
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(REQUEST_TOPIC)
    print("entering loop")

    while True:
        #print("waiting for message")
        c.wait_msg()