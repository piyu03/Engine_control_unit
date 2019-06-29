#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
import tf
import time

position = -0.135
current_time = rospy.Time()
encoder_data = 0.0

def broadcast():
    global encoder_data, position
    rospy.loginfo(position)
    current_time = rospy.Time.now()
    odom_broadcaster = tf.TransformBroadcaster()

    # rospy.loginfo(position)

    odom_quat = tf.transformations.quaternion_from_euler(0, 0, 0)
    odom_broadcaster.sendTransform(
    (position,0.02,-0.016),
    odom_quat,
    current_time,
    "base_link",
    "nut_assem"
    )

def encoder_cb(msg):
    global encoder_data, position
    encoder_data = msg.data
    position = (encoder_data / 20) * 0.00026666 - 0.135  #(encoder_data/20)*0.2666


if __name__ == '__main__':
  global position
  rospy.init_node('controller')
  rospy.Subscriber('encoder_val', Float64, encoder_cb)

  while not rospy.is_shutdown():
      broadcast()
