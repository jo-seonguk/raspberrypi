from machine import Pin
import time

from dht import DHT11 # DHT 라이브러리에서 파일을 가져옴

sensor = DHT11(Pin(17, Pin.OUT, Pin.PULL_DOWN)) # 온습도 센서를 17번핀에 연결

while True:
    temp = sensor.temperature # 온도값을 temp에 저장
    humidity = sensor.humidity # 습도값을 humidity에 저장
    print("Temperature: {}".format(temp)) # 온도값 출력
    print("Humidity: {}".format(humidity)) # 습도값 출력
    time.sleep(2)
