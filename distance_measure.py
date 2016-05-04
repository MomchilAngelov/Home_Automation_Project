import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

TRIG = 15
ECHO = 13
TRIG2 = 3
ECHO2 = 5

print ("Measure in place!")

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
	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)

	while GPIO.input(ECHO) == 0:
		pulse_start = time.time()

	while GPIO.input(ECHO) == 1:
		pulse_end = time.time()

	GPIO.output(TRIG2, True)
	time.sleep(0.00001)
	GPIO.output(TRIG2, False)

	while GPIO.input(ECHO2) == 0:
		pulse_start2 = time.time()

	while GPIO.input(ECHO2) == 1:
		pulse_end2 = time.time()

	pulse_duration = pulse_end - pulse_start
	pulse_duration2 = pulse_end2 - pulse_start2
	distance = pulse_duration * 17150
	distance2 = pulse_duration2 * 17150
	distance2 = round(distance2, 2)
	distance = round(distance, 2)

	print("Distance from sensor 1: {0} cm".format(distance))
	print("Distance from sensor 2: {0} cm".format(distance2))
	i += 1
	if i == 5:
		break
GPIO.cleanup()