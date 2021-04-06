import esp
esp.osdebug(None)

import gc
gc.collect()

from machine import Pin
import network

ssid = "XXXX"
password = "XXX"

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())
led = Pin(2, Pin.OUT)

