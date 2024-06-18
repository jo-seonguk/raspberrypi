# 조도센서

from machine import Pin, ADC   # machine 패키지에서 디지털 I/O를 위한 Pin 모듈, ADC 사용을 위한 ADC 모듈 불러옴
import time   # sleep 함수를 사용하기 위한 time 모듈 불러옴


ldr = ADC(Pin(26))   # LDR 핀을 아날로그 입력으로 구성
led = Pin(15, Pin.OUT)  # led를 15번 핀에 연결, 출력모드로 설정

while True:
    light = ldr.read_u16()  # 아날로그 값을 읽어서 light에 저장 
    print("light: " , light)   #  light 값을 출력 
    
    if light > 32768 :  # 아날로그 값이 중간 초과라면(어둡다면) LED를 켜라 
        led.value(1)
    else:   # 아날로그 값이 중간 이하라면(밝다면) LED를 꺼라
        led.value(0)
    time.sleep(1)