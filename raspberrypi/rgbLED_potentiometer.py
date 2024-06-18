from machine import Pin, PWM, ADC
import time

led1 = PWM(Pin(18))
led2 = PWM(Pin(19))
led3 = PWM(Pin(20))
led1.freq(1000)
led2.freq(1000)
led3.freq(1000)

potentiometer = ADC(26)

while True:
    #func1()

    potentiometer_value = potentiometer.read_u16()
    led1.duty_u16(potentiometer_value)
    led2.duty_u16(potentiometer_value)
    led3.duty_u16(potentiometer_value)
    



