from machine import I2C, Pin
from time import sleep
from pico_i2c_lcd import I2cLcd # I2C 통신을 위해 라이브러리 사용
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

lcd.blink_cursor_on()
print("LCD 통신 시작")
while True:
    sleep(2) # 메세지가 모두 도착하도록 잠시 대기
    lcd.clear() # LCD 내용 삭제(초기화)
    val = input() # 입력한 문자열을 val에 저장
    if len(val)<16: # 문자열의 길이가 16자 이하라면
        lcd.putstr(val) # val 값을 lcd에 출력
    else:
        print("16자 이내로 입력해주세요")
        lcd.putstr("plz 16char below")