from machine import I2C, Pin, time_pulse_us
import time
import random
from pico_i2c_lcd import I2cLcd # I2C 통신을 위해 라이브러리 사용

i2c = I2C(1, sda=Pin(26), scl=Pin(27), freq=400000)

I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)
lcd.blink_cursor_on()

print("LCD 통신 시작")

pin = Pin(14, Pin.IN, Pin.PULL_DOWN)

v = []

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

chars = [ # 0~9까지 숫자에 대한 LED 값                
#    a b c d e f g                                   
    [1,1,1,1,1,1,0], #0         ┌────a────┐
    [0,1,1,0,0,0,0], #1         │         │
    [1,1,0,1,1,0,1], #2         f         b
    [1,1,1,1,0,0,1], #3         │         │
    [0,1,1,0,0,1,1], #4         ├────g────┤
    [1,0,1,1,0,1,1], #5         │         │
    [1,0,1,1,1,1,1], #6         e         c
    [1,1,1,0,0,0,0], #7         │         │
    [1,1,1,1,1,1,1], #8         └────d────┘
    [1,1,1,1,0,1,1], #9                              
    ]                #                               

def clear():
    for j in pin_d:
        j.value(0)
    for i in pin_s: # for 문을 사용해 핀 2~9까지 8개의 핀모드 출력으로 세팅
        i.value(1)

def time_set():
    v.clear()
    now = time.localtime()
    v.append(int(now[3]/10))
    v.append(int(now[3]%10))
    v.append(int(now[4]/10))
    v.append(int(now[4]%10))
    lcd.clear()
    lcd.putstr(str(v))
#time_set()
clear()



while True:
    v.clear()
    for i in range(10000):
        v.append(i/1000)
        v.appendd100 = i%1000/100
        d10 = i%100/10
        d1 = i%10
        
        for d in range(len(pin_d)):
            for j in range(len(pin_s)):
                pin_s[j].value(chars[v[d]][j])
            pin_d[d].value(0)
            time.sleep(0.001)
            pin_d[d].value(1)
    
        
    if pin.value() == 0:
        time_set()
    
    

