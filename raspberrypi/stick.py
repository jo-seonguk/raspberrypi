from machine import Pin, ADC
import time

xAxis = ADC(Pin(27))
yAxis = ADC(Pin(26))

button = Pin(16, Pin.IN, Pin.PULL_UP) # 스위치를 입력으로 세팅하고 내부 풀업저항을 사용함

while True:
    xValue = xAxis.read_u16()
    yValue = yAxis.read_u16()
    buttonValue = button.value()
    
    print("x축: ", xValue, end=" ")
    print("y축: ", yValue, end=" ")
    print("스위치: ", buttonValue)
    time.sleep(0.1)