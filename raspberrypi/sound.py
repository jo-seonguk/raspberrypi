from machine import Pin, PWM, ADC
import time

led = PWM(Pin(22)) # led를 22번 핀에 연결, 출력으로 설정
led.freq(1000)

sound = ADC(27) 

while True:
    sound_value = sound.read_u16() # 소리감지 센서값을 읽어서변수 sound_value에 저장
    led.duty_u16(sound_value) # PWM을 발생 시킴
    print(sound_value) # 센서값 출력
    time.sleep(1)
