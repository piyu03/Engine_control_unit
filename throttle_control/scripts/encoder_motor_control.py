#!/usr/bin/env python

import rospy
import RPi.GPIO as GPIO
from std_msgs.msg import Float64

M1pwm_pin = 13
M1dir_pin = 5
speed = 100
currentSpeed = 0
givenSpeed = 0
motorRunning = False

GPIO.setmode(GPIO.BOARD)

GPIO.setup(M1pwm_pin, GPIO.OUT)
GPIO.setup(M1dir_pin, GPIO.OUT)

GPIO.output(M1pwm_pin, GPIO.LOW)
GPIO.output(M1dir_pin, GPIO.LOW)

motor = GPIO.PWM(M1pwm_pin, 50)
motor.start(0)

def motor_control():
    global currentSpeed, givenSpeed, speed, motor, M1dir_pin, motorRunning
    # rospy.loginfo(givenSpeed)
    if(givenSpeed != currentSpeed):
        if not motorRunning:
            motor.start(0)
            motor.ChangeDutyCycle(speed)
            motorRunning=True

        if givenSpeed > currentSpeed:
            GPIO.output(M1dir_pin, GPIO.HIGH)
        else:
            GPIO.output(M1dir_pin, GPIO.LOW)
    else:
        if(motorRunning):
            motor.stop()
            motorRunning = False


def encoder_val_callback(msg):
    global currentSpeed, givenSpeed, speed, motor, M1dir_pin, motorRunning
    currentSpeed = msg.data

def control_effort_callback(msg):
    global givenSpeed
    givenSpeed = msg.data
    rospy.loginfo(msg.data)

rospy.init_node('encoder_motor_control')
rospy.Subscriber('encoder_val', Float64, encoder_val_callback)
rospy.Subscriber('control_effort', Float64, control_effort_callback)

while not rospy.is_shutdown():
    motor_control()

GPIO.cleanup()
