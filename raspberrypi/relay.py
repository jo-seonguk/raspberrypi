from machine import Pin
import time

pin1 = Pin(27,Pin.OUT)     #릴레이
pin2 = Pin(16,Pin.IN, Pin.PULL_DOWN)      #버튼


while True:
    if pin2.value(1):
        pin1.value(0)
    else:
        pin1.value(0)