#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32
from std_msgs.msg import Float64
from std_msgs.msg import Int32
from std_msgs.msg import Int64
from std_msgs.msg import String
import tf
import time

encoder_data = 0
position = 0.0
set_position = 5.0
e_position = 0.0

set_speed = 0
feedback_speed = 0.0
direction = -0.135
current_time = rospy.Time()
# e_speed_sum = 0.0
# e_speed_pre = 0.0
pwm_pulse = 0.0
kp = 0.0
# ki =
# kd =

def speed_cb(msg):
    global set_speed, kp
    set_speed = msg.data
    kp = 100.0 / set_speed
    # rospy.loginfo(set_speed)

def feedback_cb(msg):
    global feedback_speed
    feedback_speed = msg.data
    # print("controlle_val=",feedback_speed)

def encoder_cb(msg):
    global encoder_data
    encoder_data = msg.data
    rospy.loginfo(position)

def encoder_pid():
    global position, encoder_data, e_position, set_position
    position = encoder_data * 0.266666
    e_position = set_position - position
    if (e_position > 0):
        pub.publish(100.0)
    elif (e_position < 0):
        pub.publish(-100.0)

def pid_control():
  global set_speed, feedback_speed, direction, e_speed, e_speed_sum, e_speed_pre, kp, ki, kd, pwm_pulse
  current_time = rospy.Time.now()
  odom_broadcaster = tf.TransformBroadcaster()
  e_speed = set_speed - feedback_speed
  pwm_pulse = e_speed * kp
  # PID code. need to be modified based on the required application.
  # e_speed = set_speed - feedback_speed;
  # pwm_pulse = e_speed*kp + e_speed_sum*ki + (e_speed - e_speed_pre)*kd;
  # e_speed_pre = e_speed;  //save last (previous) error
  # e_speed_sum += e_speed; //sum of error
  # if (e_speed_sum >4000) e_speed_sum = 4000;
  # if (e_speed_sum <-4000) e_speed_sum = -4000;

  # rospy.loginfo(pwm_pulse)
  if (pwm_pulse > 0):
    pub.publish(pwm_pulse)
    # rospy.loginfo("Move cw")
    odom_quat = tf.transformations.quaternion_from_euler(0, 0, 0)
    odom_broadcaster.sendTransform(
        (direction,0.02,-0.016),
        odom_quat,
        current_time,
        "base_link",
        "nut_assem"
    )
    direction += 0.00012

  elif (pwm_pulse < 0):
    pub.publish(pwm_pulse)
    # rospy.loginfo("Move ccw")
    odom_quat = tf.transformations.quaternion_from_euler(0, 0, 0)
    odom_broadcaster.sendTransform(
        (direction,0.02,-0.016),
        odom_quat,
        current_time,
        "base_link",
        "nut_assem"
    )
    direction -= 0.00012

  else:
    pub.publish(pwm_pulse)
    odom_quat = tf.transformations.quaternion_from_euler(0, 0, 0)
    odom_broadcaster.sendTransform(
        (direction,0.02,-0.016),
        odom_quat,
        current_time,
        "base_link",
        "nut_assem"
    )

if __name__ == '__main__':
  rospy.init_node('controller')
  pub = rospy.Publisher('driver_val', Float32, queue_size=20)
  rospy.Subscriber('speed_raw', Int32, speed_cb)
  rospy.Subscriber('feedback_val', Float32, feedback_cb)
  rospy.Subscriber('encoder_val', Int64, encoder_cb)
  rate = rospy.Rate(60)
  while not rospy.is_shutdown():
    encoder_pid()
    rate.sleep()
