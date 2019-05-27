#!/usr/bin/env python2

import rospy
from std_msgs.msg import Int16
import time
import serial


def init():
    rospy.init_node("txco_node", anonymous=False)

def port():
    return rospy.get_param('~port')

def baudrate():
    return rospy.get_param('~baudrate')

def co2talker():
    pub = rospy.Publisher("txco_publisher", Int16, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        co2_val = int(ser.readline())
        pub.publish(co2_val)
        rate.sleep()

if __name__ == "__main__":
    try:
        init()
        ser = serial.Serial(port(), baudrate(), parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE, bytesize = serial.EIGHTBITS)
        time.sleep(1)
        co2talker()
        
    except rospy.ROSInterruptException:
        ser.close()
        pass
