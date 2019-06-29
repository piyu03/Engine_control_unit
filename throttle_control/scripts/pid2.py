#!/usr/bin/env python

import rospy
import RPi.GPIO as GPIO
from std_msgs.msg import Float64

Kp = 1.65
Ki = 0.001
Kd = 0.03

MAXIMUM_LIMIT = 500
MINIMUM_LIMIT = 0

feedback = 0
setpoint = 0

def setpoint_callback(msg):
    global setpoint
    setpoint = msg.data

def feedback_callback(msg):
    global feedback
    feedback = msg.data

def setLimits(val):
    if val > MAXIMUM_LIMIT:
        return MAXIMUM_LIMIT

    if val < MINIMUM_LIMIT:
        return MINIMUM_LIMIT

    return val

rospy.init_node('pid')
rospy.Subscriber('setpoint', Float64, setpoint_callback)
rospy.Subscriber('feedback_val', Float64, feedback_callback)

pub = rospy.Publisher('control_effort',Float64,queue_size=10)

rate = rospy.Rate(60)

while not rospy.is_shutdown():
    error = (setpoint - feedback)

    error = error * Kp

    error = setLimits(error)

    print(error)

    control_effort = Float64()
    control_effort.data = feedback + error
    pub.publish(control_effort)
    rate.sleep()
