from sensors.dht11_sensor import read_temperature
from sensors.max30102_sensor import setup_max30102, read_heart_rate
from sensors.mpu6050_sensor import read_motion
from utils.signal_processing import (
    classify_activity,
    classify_temperature,
    classify_heart_rate
)
from alerts.twilio_alert import send_alert
import time

setup_max30102()

print("Smart Livestock Health Monitoring System Started")

while True:
    temp = read_temperature()
    hr = read_heart_rate()
    ax, ay, az, gx, gy, gz = read_motion()

    activity = classify_activity(ax, ay, az)
    temp_status = classify_temperature(temp)
    hr_status = classify_heart_rate(hr)

    print(f"Temp: {temp} °C ({temp_status})")
    print(f"Heart Rate: {hr} BPM ({hr_status})")
    print(f"Activity: {activity}")
    print("-" * 40)

    if temp_status != "Normal" or hr_status != "Normal":
        send_alert(temp, hr, activity)

    time.sleep(60)  # Paper says: SMS every 60 minutes (configurable)

