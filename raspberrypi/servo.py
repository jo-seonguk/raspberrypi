from machine import Pin, PWM, ADC
from time import sleep

adc = ADC(Pin(26))
servoPin = PWM(Pin(16))
servoPin.freq(50)

def servo(degrees):
    if degrees > 180:
        degrees = 180
    elif degrees < 0:
        degrees = 0
    maxDuty = 9000
    minDuty = 1000
    newDuty = minDuty + (maxDuty-minDuty)*(degrees/180)
    servoPin.duty_u16(int(newDuty))
    
while True:
    value = adc.read_u16()
    degree = value*180/65500
    print(degree)
    servo(degree)
    sleep(0.005)
