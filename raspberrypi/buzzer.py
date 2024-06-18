from machine import Pin, PWM
import time
button = Pin(14, Pin.IN, Pin.PULL_UP)
buzzerPIN = PWM(Pin(11))

def tone(frequency):
    buzzerPIN.duty_u16(30000)
    buzzerPIN.freq(frequency)
    
def noTone():
    buzzerPIN.duty_u16(0)
    
melody = [262, 294, 330, 349, 392, 440, 494, 523]

while True:
    for i in range(len(melody)):
        if button.value() == 1:
            noTone()
        else:
            tone(melody[i])
        time.sleep(0.3)
    noTone()