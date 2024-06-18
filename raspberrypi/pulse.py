from machine import Pin, time_pulse_us
import time

pin1 = Pin(16,Pin.OUT)
pin2 = Pin(17,Pin.IN)

while True:
    pin1.value(1)
    time.sleep_us(10)
    pin1.value(0)

    pulse_time = machine.time_pulse_us(pin2, 1, 100000)
    distance = ((pulse_time * 340) /10000)/2
    print(distance)
    time.sleep(1)
    
