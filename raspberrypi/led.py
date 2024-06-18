from machine import Pin, PWM, ADC
import time

led1 = PWM(Pin(18))
led2 = PWM(Pin(19))
led3 = PWM(Pin(20))
led4 = PWM(Pin(22))
led1.freq(1000)
led2.freq(1000)
led3.freq(1000)
led4.freq(1000)
potentiometer = ADC(26)

def func1():
    for duty in range(65025):
        led1.duty_u16(duty)
        led2.duty_u16(duty)
        led3.duty_u16(duty)
        time.sleep(0.0001)
    for duty in range(65025, 0, -1):
        led1.duty_u16(duty)
        led2.duty_u16(duty)
        led3.duty_u16(duty)
        time.sleep(0.0001)

while True:
    func1()

    potentiometer_value = potentiometer.read_u16()
    led4.duty_u16(potentiometer_value)
    


