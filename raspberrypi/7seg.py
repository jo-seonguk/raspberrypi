from machine import Pin
from time import sleep

pins = [ # 배열로 핀 연결
    Pin(16, Pin.OUT),
    Pin(17, Pin.OUT),
    Pin(18, Pin.OUT),
    Pin(19, Pin.OUT),
    Pin(13, Pin.OUT),
    Pin(14, Pin.OUT),
    Pin(15, Pin.OUT),
    
    Pin(12, Pin.OUT)
    ]

chars = [ # 0~9까지 숫자에 대한 LED 값
    [1,0,0,0,0,0,0,0], #0
    [1,1,1,0,0,1,1,0], #1
    [0,1,0,0,1,0,0,0], #2
    [0,1,0,0,0,0,1,0], #3
    [0,0,1,0,0,1,1,0], #4
    [0,0,0,1,0,0,1,0], #5
    [0,0,0,1,0,0,0,0], #6
    [1,1,0,0,0,1,1,0], #7
    [0,0,0,0,0,0,0,0], #8
    [0,0,0,0,0,0,1,0], #9
    ]

def clear():
    for i in pins: # for 문을 사용해 핀 2~9까지 8개의 핀모드 출력으로 세팅
        i.value(1)
clear()

while True:
    for i in range(len(chars)): # 이중 for문을 이용해 led로 숫자 출력
        for j in range(len(pins)):
            pins[j].value(chars[i][j])
            
        sleep(1) # 1초간 딜레이