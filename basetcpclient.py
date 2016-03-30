import socket
import sys

class BaseTCPClient:

	def __init__(self, portnum, data):
		self.HOST = "127.0.0.1"
		self.PORT = int(portnum)
		self.sock = None

		# self.data = " ".join(sys.argv[2:])
		self.data = data

	def open_connection(self):
		# Create a socket (SOCK_STREAM means a TCP socket)
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def send_data(self):
		try:
			# Connect to server and send data
			self.sock.connect((self.HOST, self.PORT))
			self.sock.sendall(bytes(self.data + "\n", "utf-8"))

			# Receive data from the server and shut down
			received = str(self.sock.recv(1024), "utf-8")
		finally:
			self.sock.close()

		print("Sent:     {}".format(self.data))
		print("Received: {}".format(received))