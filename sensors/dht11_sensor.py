import dht11
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

DHT_PIN = 4
sensor = dht11.DHT11(DHT_PIN)

def read_temperature():
    while True:
        result = sensor.read()
        if result.is_valid():
            return result.temperature
        time.sleep(1)
