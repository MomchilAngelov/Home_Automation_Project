import datetime

low_time_hour = 20
low_time_minute = 30

high_time_hour = 4
high_time_minute = 30

def time_threshhold():
	print("Its night m8")

def get_current_time():
	time = str(datetime.datetime.now())
	time = time.split(" ")
	time[1] = time[1].split(".")
	curr_time = time[1][0].split(":")

	curr_hour = int(curr_time[0])
	curr_min = int(curr_time[1])
	return curr_hour, curr_min

def is_in_threshhold(hour, minute):
	global low_time_hour
	global low_time_minute
	global high_time_minute
	global high_time_hour

	if hour >= low_time_hour:
		if hour == low_time_hour:
			if minute >= low_time_minute:
				return 1
			else:
				return 0
		else:
			return 1

	if hour <= high_time_hour:
		if hour == high_time_hour:
			if minute <= high_time_hour:
				return 1
			else:
				return 0
		else:
			return 1
	return 0

hour, minute = get_current_time()
if (is_in_threshhold(hour, minute)):
	time_threshhold()