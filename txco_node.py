#!/usr/bin/env python

import rospy
from std_msgs.msg import Int16
import time
import serial

def co2talker():
    pub = rospy.Publisher("txco_publisher", Int16, queue_size=10)
    rospy.init_node("txco_node", anonymous=False)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        co2_val = int(ser.readline())
        pub.publish(co2_val)
        rate.sleep()

if __name__ == "__main__":
    try:
        ser = serial.Serial("/dev/ttyACM0", baudrate = 9600, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE, bytesize = serial.EIGHTBITS)
        time.sleep(1)
        
        co2talker()
    except rospy.ROSInterruptException:
        ser.close()
        pass
