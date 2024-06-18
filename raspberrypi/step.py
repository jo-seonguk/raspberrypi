from machine import Pin # machine 패키지에서 디지털 I/O를 위한 Pin 모듈 불러옴
import time # sleep 함수를 사용하기 위한 time 모듈 불러옴

pin1 = Pin(16,Pin.OUT)
pin2 = Pin(17,Pin.OUT)
pin3 = Pin(15,Pin.OUT)
pin4 = Pin(14,Pin.OUT)

SEQUENCE  = [
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1],
]

steps = 2048 # 모터의 스텝수 2048=1바퀴, 1024=반바퀴

def move_stepper(direction, steps):
    # 입력핀 설정
    pins = [pin1, pin2, pin3, pin4,]

    # 방향 설정
    if direction == 'forward':
        sequence = SEQUENCE
    
    elif direction == 'backward':
       sequence = list(reversed(SEQUENCE))

    # Loop through the specified number of steps
    for i in range(steps):

        # Set the input pins based on the current step
        for j in range(len(pins)):
            pins[j].value(sequence[i%4][j])

        # Delay between steps
        time.sleep(0.005)

while True:
    # 시계방향으로 스텝 수만큼 이동
    move_stepper('forward', steps)
    time.sleep(0.5) # 모터 정지 후 잠시 대기 

    # 반시계방향으로 스텝 수만큼 이동
    move_stepper('backward', steps)
    time.sleep(0.5) # 모터 정지 후 잠시 대기