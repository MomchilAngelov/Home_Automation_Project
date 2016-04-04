class RequestManager:

	def __init__(self):
		self.movementDir = []

	def get_humidity(self):
		return 0.6611

	def get_light(self):
		return 1.51532

	def record_movement(self, direction):
		if direction is 1:
			# Left -> Right
		elif direction is 2:
			# Right -> Left