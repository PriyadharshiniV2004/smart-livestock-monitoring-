import smbus
import time

MPU6050_ADDR = 0x68
PWR_MGMT_1 = 0x6B
ACCEL_XOUT_H = 0x3B
GYRO_XOUT_H = 0x43

bus = smbus.SMBus(1)
bus.write_byte_data(MPU6050_ADDR, PWR_MGMT_1, 0)

def read_raw(register):
    high = bus.read_byte_data(MPU6050_ADDR, register)
    low = bus.read_byte_data(MPU6050_ADDR, register + 1)
    value = (high << 8) | low
    if value > 32768:
        value -= 65536
    return value

def read_motion():
    ax = read_raw(ACCEL_XOUT_H) / 16384.0
    ay = read_raw(ACCEL_XOUT_H + 2) / 16384.0
    az = read_raw(ACCEL_XOUT_H + 4) / 16384.0

    gx = read_raw(GYRO_XOUT_H) / 131.0
    gy = read_raw(GYRO_XOUT_H + 2) / 131.0
    gz = read_raw(GYRO_XOUT_H + 4) / 131.0

    return ax, ay, az, gx, gy, gz
