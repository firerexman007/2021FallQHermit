# use Python 3
import socket
from time import sleep

# constants
ZERO = 0.025
ONE = 0.1

# set the port for client connections
port = 1337

# create the socket and bind it to the port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", port))

# listen for clients
# this is a blocking call
s.listen(0)
print("Server is listening...")

# a client has connected!
c, addr = s.accept()

# set the message
msg = ""
for i in range(10):
	msg += "Testing Testing Testing "
msg += "\n"

# set the covert message
covert = "secret message" + "EOF"

# convert cover msg to binary
covert_bin = ''
for i in covert:
	covert_bin += ''.join(format(ord(i), '08b'))

# send the message, one letter at a time with delays for the covert message
for i in msg:
	n = 0
	c.send(i.encode())
	if covert_bin[n] == "0":
		sleep(ZERO)
	else:
		sleep(ONE)
	n = (n + 1) % len(covert_bin)

# send EOF and close the connection to the client
c.send("EOF".encode())
print("Message sent...")
c.close()
