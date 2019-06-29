#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64

vehicle_speed = 400

if __name__ == '__main__':
    rospy.init_node('speed')
    pub = rospy.Publisher('setpoint', Float64, queue_size=10)
    rate = rospy.Rate(60)
    # vehicle_speed = input("Enter speed of the vehicle:")


    while not rospy.is_shutdown():
        rate.sleep()
pub.publish(vehicle_speed)
