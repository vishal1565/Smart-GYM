from mpu6050 import mpu6050
from time import sleep
import csv
sensor = mpu6050(0x68)
print " waiting for the sensor to callibrate..."
sleep(2)

#Storing data in Angle_measure.csv with features: accl_x, accl_y, accl_z, gyro_x, gyro_y, gyro_z, Temperature
with open('Angle_measure.csv','a') as f:
    pen=csv.writer(f)
    while True:
        accel_data = sensor.get_accel_data()
        gyro_data = sensor.get_gyro_data()
        temp = sensor.get_temp()
        pen.writerow([str(accel_data['x']),str(accel_data['y']),str(accel_data['z']),str(gyro_data['x']),str(gyro_data['y']),str(gyro_data['z']),str(temp)])
        print("Accelerometer data")
        print("x: " + str(accel_data['x']))
        print("y: " + str(accel_data['y']))
        print("z: " + str(accel_data['z']))
        print("Gyroscope data")
        print("x: " + str(gyro_data['x']))
        print("y: " + str(gyro_data['y']))
        print("z: " + str(gyro_data['z']))
        print("Temp: " + str(temp) + " C")
        sleep(2)
