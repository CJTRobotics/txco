#!/usr/bin/env python2

import rospy
from std_msgs.msg import Int16
import time
import serial


class Node:

    def __init__(self):
        self.init = rospy.init_node("txco_node", anonymous=False)
        self.port = rospy.get_param('~port')
        self.baudrate = rospy.get_param('~baudrate')
        self.ser = serial.Serial(self.port, self.baudrate, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, \
                        bytesize=serial.EIGHTBITS)

    def co2talker(self):
        pub = rospy.Publisher("txco_publisher", Int16, queue_size=10)
        rate = rospy.Rate(10) # 10hz

        while not rospy.is_shutdown():
            co2_val = int(self.ser.readline())
            pub.publish(co2_val)
            rate.sleep()

    def main(self):
        try:
            time.sleep(1)
            self.co2talker()
        except rospy.ROSInterruptException:
            self.ser.close()
            pass


if __name__ == "__main__":
    Node().main()

