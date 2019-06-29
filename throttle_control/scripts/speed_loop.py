#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64

speed = 0.0

def speed_cb(msg):
    global speed
    speed = msg.data

if __name__ == '__main__':
  rospy.init_node('controller')
  pub = rospy.Publisher('setpoint', Float64, queue_size=20)
  rospy.Subscriber('set_speed', Float64, speed_cb)
  rate = rospy.Rate(60)

  while not rospy.is_shutdown():
    pub.publish(speed)
    rospy.loginfo(speed)
    rate.sleep()
