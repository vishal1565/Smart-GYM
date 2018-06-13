import smbus
import math
import os
from time import sleep
import csv

power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

def read_byte(reg):
    return bus.read_byte_data(address, reg)

def read_word(reg):
    h = bus.read_byte_data(address, reg)
    l = bus.read_byte_data(address, reg)
    value = (h << 8) + l
    return value

def read_word_2c(reg):
    val = read_word(reg)
    if val >= 0x8000:
        return -((65535 - val) + 1)
    else:
        return val

def dist(a,b): return math.sqrt((a*a)+(b*b))

def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y, z))
    return -math.degrees(radians)

def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x, z))
    return math.degrees(radians)


with open('Angle_measure.csv','a') as f:
    pen = csv.writer(f)
    while True:
        bus = smbus.SMBus(1)
        address = 0x68

        bus.write_byte_data(address, power_mgmt_1, 0)


        #Gyroscope Part

        g_xout = read_word_2c(0x43)
        g_yout = read_word_2c(0x45)
        g_zout = read_word_2c(0x47)

        #print("Gyro(x,y,z):", g_xout/131, g_yout/131, g_zout/131)


        #Accelerometer Part

        a_xout = read_word_2c(0x3b)
        a_yout = read_word_2c(0x3d)
        a_zout = read_word_2c(0x3f)

        #print("Accl(x,y,z):",a_xout/16384.0, a_yout/16384.0, a_zout/16384.0)

        print("X Rotation: ",get_x_rotation(a_xout, a_yout, a_zout))
        print("Y Rotation: ",get_y_rotation(a_xout, a_yout, a_zout))
        pen.writerow([get_x_rotation(a_xout, a_yout, a_zout),get_y_rotation(a_xout, a_yout, a_zout)])
        print("********************************************************************")
        sleep(1)
