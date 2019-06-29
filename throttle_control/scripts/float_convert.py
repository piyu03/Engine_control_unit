#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64,Float32
import time

m = Float64()
pub = None

def callback(msg):
    global m
    m.data = msg.data

if __name__ == '__main__':
    global pub, m
    rospy.init_node('float_converter')
    pub = rospy.Publisher('feedback_val2', Float64, queue_size=10)
    rospy.Subscriber('feedback_val', Float64,callback)
    rate = rospy.Rate(60) #60 Hz

    while not rospy.is_shutdown():
        rate.sleep()
        pub.publish(m)
