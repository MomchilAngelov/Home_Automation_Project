import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BOARD)

alarm = False
alarm_pin = 31
alarm_set = True
GPIO.setup(alarm_pin, GPIO.OUT)

def start_alarm():
	global alarm_set
	alarm_set = True

def stop_alarm():
	global alarm_set
	global alarm_pin
	alarm_set = False
	GPIO.output(alarm_pin, alarm_set)

'''
is_lit = False
lamp_pin = 22
GPIO.setup(lamp_pin, GPIO.OUT)

def light_lamp():
	global is_lit
	is_lit = not is_lit
	GPIO.output(lamp_pin, is_lit)
'''

lamp = False
pin = 29

TRIG = 11
ECHO = 16
TRIG2 = 15
ECHO2 = 13
left_to_right = 0
right_to_left = 0
counter = 0
number_of_tries = 30

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(TRIG2, GPIO.OUT)
GPIO.setup(ECHO2, GPIO.IN)
GPIO.setup(pin, GPIO.OUT)

GPIO.output(TRIG, False)
GPIO.output(TRIG2, False)
i = 0

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

	if distance2 < 5 and distance > 5 and right_to_left == 0:
		GPIO.output(pin, False)
		left_to_right = 1
		counter = 0
		print("OUT")
	if distance < 5 and distance2 > 5 and left_to_right == 0:
		GPIO.output(pin, True)
		right_to_left = 1
		counter = 0
		print("IN")
	if distance > 5 and distance2 > 5:
		print("IDLE")
		counter += 1
		if counter > 3:
			left_to_right = 0
			right_to_left = 0

	return distance, distance2

while True:
	'''
	time.sleep(1)
	print("Distance from one: {0}cm;\nDistance from two: {1}cm;\n".format(distance_from_one, distance_from_two))
	i += 1
	if i == number_of_tries:
		break
	light_lamp()	
	'''
	i += 1
	if i%2 == 0:
		start_alarm()
	else:
		stop_alarm()

	distance_from_one, distance_from_two = get_value_distance()
	if distance_from_two < 15 and distance_from_one < 15 and alarm_set:
		GPIO.output(alarm_pin, alarm_set)
	sleep(1)

GPIO.cleanup()