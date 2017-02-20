# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import gc
import webrepl
import elServer
webrepl.start()
gc.collect()
elServer.start()