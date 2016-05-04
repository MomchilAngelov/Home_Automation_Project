import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BOARD)

TRIG = 11
ECHO = 16
TRIG2 = 15
ECHO2 = 13
left_to_right = 0
right_to_left = 0
counter = 0
number_of_tries = 10

def get_value_distance():
	global TRIG
	global ECHO
	global TRIG2
	global ECHO2
	global left_to_right
	global right_to_left
	global counter

	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)
	while GPIO.input(ECHO) == 0:
		pulse_start = time.time()

	while GPIO.input(ECHO) == 1:
		pulse_end = time.time()
	pulse_duration = pulse_end - pulse_start
	distance = pulse_duration * 17150
	distance = int(distance)

	GPIO.output(TRIG2, True)
	time.sleep(0.00001)
	GPIO.output(TRIG2, False)

	while GPIO.input(ECHO2) == 0:
		pulse_start2 = time.time()

	while GPIO.input(ECHO2) == 1:
		pulse_end2 = time.time()

	pulse_duration2 = pulse_end2 - pulse_start2
	distance2 = pulse_duration2 * 17150
	distance2 = int(distance2)

	if distance2 < 10 and distance > 10 and right_to_left == 0:
		print("Moving left to right!(out)")
		left_to_right = 1
		counter = 0
	if distance < 10 and distance2 > 10 and left_to_right == 0:
		print("Moving right to left! (in)")
		right_to_left = 1
		counter = 0
	if distance > 10 and distance2 > 10:
		counter += 1
		if counter > 3:
			left_to_right = 0
			right_to_left = 0

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
	time.sleep(1)
	distance_from_one, distance_from_two = get_value_distance()
	print("Distance from one: {0}cm;\nDistance from two: {1}cm;\n".format(distance_from_one, distance_from_two))
	i += 1
	if i == number_of_tries:
		#break
		pass
GPIO.cleanup()
