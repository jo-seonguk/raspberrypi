from machine import Pin
from time import sleep
import random

pin_s = [ # 배열로 핀 연결
    Pin(0, Pin.OUT),
    Pin(1, Pin.OUT),
    Pin(2, Pin.OUT),
    Pin(3, Pin.OUT),
    Pin(4, Pin.OUT),
    Pin(5, Pin.OUT),
    Pin(6, Pin.OUT),
    ]

pin_d = [
    Pin(21, Pin.OUT),
    Pin(20, Pin.OUT),
    Pin(19, Pin.OUT),
    Pin(18, Pin.OUT)
    ]

chars = [ # 0~9까지 숫자에 대한 LED 값                  ────a─────
#    a b c d e f g                                   │           │
    [1,1,1,1,1,1,0], #0                              │           │
    [0,1,1,0,0,0,0], #1                              f           b
    [1,1,0,1,1,0,1], #2                              │           │
    [1,1,1,1,0,0,1], #3                              │           │
    [0,1,1,0,0,1,1], #4                               ─────g─────
    [1,0,1,1,0,1,1], #5                              │           │
    [1,0,1,1,1,1,1], #6                              │           │
    [1,1,1,0,0,0,0], #7                              e           c
    [1,1,1,1,1,1,1], #8                              │           │
    [1,1,1,1,0,1,1], #9                              │           │
    ]                #                                ─────d─────

def clear():
    
    for j in pin_d:
        j.value(0)
    for i in pin_s: # for 문을 사용해 핀 2~9까지 8개의 핀모드 출력으로 세팅
        i.value(1)
clear()

v = []
for i in range(4):
    v.append(random.randint(0,9))
    
print(v)
while True:
    for d in range(len(pin_d)):
        #show_digit(d)
        for j in range(len(pin_s)):
            pin_s[j].value(chars[v[d]][j])
        pin_d[d].value(0)
        sleep(0.001)
        pin_d[d].value(1)