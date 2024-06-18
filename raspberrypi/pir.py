from machine import Pin, time_pulse_us
import time

pin1 = Pin(16,Pin.IN)

while True:
    if pin1.value() == 1:
        t = time.localtime()
        print (t)
    else:
        print("x")
    time.sleep(0.05)
    