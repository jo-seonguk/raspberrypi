from machine import I2C, Pin
import time
from pico_i2c_lcd import I2cLcd 

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

lcd.blink_cursor_on()
pin = Pin(15, Pin.IN, Pin.PULL_DOWN)

matrix_keys = [ # 배열로 각 버튼을 숫자나 문자로 대응
    ['0', '1', '2', '3'],
    ['4', '5', '6', '7'],
    ['8', '9', 'A', 'B'],
    ['C', 'D', 'E', 'F']
    ]

keypad_rows = [13,12,11,10] # 행(Row)가 연결된 Pico GPIO 번호
keypad_columns = [18,19,20,21] # 열(Column)가 연결된 Pico GPIO 번호

col_pins = []
row_pins = []

for x in range(0,4):
    row_pins.append(Pin(keypad_rows[x], Pin.OUT))
    row_pins[x].value(1)
    col_pins.append(Pin(keypad_columns[x], Pin.IN, Pin.PULL_DOWN))
    col_pins[x].value(0)
    
print("Please enter a key from the keypad")
a = '0x'
def scankeys():
    global a
    
    for row in range(4):
        for col in range(4):
            row_pins[row].high()
            key = None
            if pin.value == 0:
                print('3')
                lcd.clear()
                lcd.putstr(str(int(a,16)))
                a = '0x'
            if col_pins[col].value() == 1: # 입력된 값이 있으면, 출력
                print(matrix_keys[row][col])
                lcd.clear()
                if len(a) == 18:
                    print('최대 16자리까지 입력')
                    lcd.clear()
                    lcd.putstr(str(int(a,16)))
                    a = '0x'
                else:
                    a += str(matrix_keys[row][col])
                    print(a)
                    print(int(a, 16))
                    lcd.putstr(a)
                key_press = matrix_keys[row][col]
                time.sleep(0.3)
                    
        row_pins[row].low()

while True:
    scankeys()