#!/usr/bin/env python

RPI = True

import rospy
from std_msgs.msg import Float64
import time

sensor = 3

if RPI:
  import RPi.GPIO as GPIO
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(sensor, GPIO.IN)

last_time = rospy.Time()
state = 0
prevState = 0
counter = 0.0
sensor_val = 0.0
val = 0
rpm = 0.0

def get_rpm():
  global current_time, last_time, state, prevState, counter, sensor, sensor_val, rpm

  current_time = rospy.Time.now()

  if RPI:
    sensor_val = GPIO.input(sensor)

#  print (sensor_val)

  if (sensor_val == 1):
    state = 1
  elif (sensor_val == 0):
    state = 0

  if (state != prevState):
    if(state == 1):
      counter += 1
    prevState = state

  val = (current_time - last_time).to_sec()
  # print (counter)

  if (counter >= 2):
    rpm = (60.0*counter) / (val)
#    print (rpm, val, counter)
    counter = 0
    last_time = current_time

  if (val > 2):
    rpm = 10
  rospy.loginfo(rpm)
  pub.publish(rpm)
  # print (rpm)
#  if (val > 1):
#    print counter * 60
#    counter = 0
#    last_time = current_time


if __name__ == '__main__':
  rospy.init_node('feedback_val')
  pub = rospy.Publisher('feedback_val', Float64, queue_size=10)

  last_time = rospy.Time.now()
  while not rospy.is_shutdown():
    get_rpm()

GPIO.cleanup()
rospy.loginfo("GPIO Cleanup done")
