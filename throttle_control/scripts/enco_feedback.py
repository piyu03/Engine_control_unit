#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
from RPi import GPIO

clk_pin = 11
dt_pin = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(clk_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

clkLastState = GPIO.input(clk_pin)
counter = 0

rospy.init_node('encoder_val')
pub = rospy.Publisher('encoder_val', Float64, queue_size=10)

while not rospy.is_shutdown():
  clkState = GPIO.input(clk_pin)
  dtState = GPIO.input(dt_pin)

  if clkState != clkLastState:
    if dtState != clkState:
      counter += 1
    else:
      counter -= 1

    clkLastState = clkState
    rpm = Float64()
    rpm.data = (counter * 20) #convert counter to 0-1500 RPM
    pub.publish(rpm)
    rospy.loginfo(rpm.data)

GPIO.cleanup()
rospy.loginfo("GPIO Cleanup done")
