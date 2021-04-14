#!/usr/bin/python3

import RPi.GPIO as GPIO
import datetime
import time

pump = 8

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pump, GPIO.OUT)

f = open("last_watered.txt", "w")
f.write("Last watered {}".format(datetime.datetime.now()))
f.close()

GPIO.output(pump, GPIO.LOW)
time.sleep(10)
GPIO.output(pump, GPIO.HIGH)

GPIO.cleanup()
