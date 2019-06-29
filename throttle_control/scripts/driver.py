#!/usr/bin/env python

RPI = True

import rospy
from std_msgs.msg import Float64
from std_msgs.msg import Float32
import time

if RPI:
  import RPi.GPIO as GPIO

pwm_val = 0

if RPI:
  GPIO.setmode(GPIO.BOARD)

  M1pwm = 13
  M1dir = 5  # Motor 1

  GPIO.setup(M1pwm, GPIO.OUT)
  GPIO.setup(M1dir, GPIO.OUT)

  GPIO.output(M1pwm, GPIO.LOW)
  GPIO.output(M1dir, GPIO.LOW)

  pwm1 = GPIO.PWM(M1pwm, 50)
  pwm1.start(0)
else:
  print("Simulated setup done!")

def motor_run():
  global pwm_val
  # rospy.loginfo(pwm_val)
  if RPI:
    if (pwm_val > 0):
      pwm1.start(0)
      pwm1.ChangeDutyCycle(pwm_val)
      GPIO.output(M1dir, GPIO.HIGH)

    elif (pwm_val < 0):
      pwm1.start(0)
      pwm_val = pwm_val * (-1)
      pwm1.ChangeDutyCycle(pwm_val)
      GPIO.output(M1dir, GPIO.LOW)

    elif (pwm_val == 0):
      pwm1.stop()
      GPIO.output(M1dir, GPIO.LOW)

def callback(msg):
  global pwm_val
  pwm_val = msg.data
  pwm_val = int(pwm_val)

if __name__ == '__main__':
  rospy.init_node('driver')
  rospy.Subscriber('driver_val', Float32, callback)
  rate = rospy.Rate(60)

  while not rospy.is_shutdown():
    motor_run()
    rate.sleep()

  if RPI:
    GPIO.cleanup()
