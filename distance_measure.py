import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BOARD)

TRIG = 11
ECHO = 16
TRIG2 = 15
ECHO2 = 13

def get_value():
	global TRIG
	global ECHO
	global TRIG2
	global ECHO2


	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)
	while GPIO.input(ECHO) == 0:
		pulse_start = time.time()

	while GPIO.input(ECHO) == 1:
		pulse_end = time.time()
	pulse_duration = pulse_end - pulse_start
	distance = pulse_duration * 17150
	distance = round(distance, 2)


	GPIO.output(TRIG2, True)
	time.sleep(0.00001)
	GPIO.output(TRIG2, False)

	while GPIO.input(ECHO2) == 0:
		pulse_start2 = time.time()

	while GPIO.input(ECHO2) == 1:
		pulse_end2 = time.time()

	pulse_duration2 = pulse_end2 - pulse_start2
	distance2 = pulse_duration2 * 17150
	distance2 = round(distance2, 2)
	return distance, distance2


GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(TRIG2, GPIO.OUT)
GPIO.setup(ECHO2, GPIO.IN)

GPIO.output(TRIG, False)
GPIO.output(TRIG2, False)
print("Waiting to settle!")
i = 0
while True:
	time.sleep(2)
	distance_from_one, distance_from_two = get_value()
	print("Distance from one: {0}cm;\nDistance from two: {1}cm;\n".format(distance_from_one, distance_from_two))
	i += 1
	if i == 5:
		break
GPIO.cleanup()
