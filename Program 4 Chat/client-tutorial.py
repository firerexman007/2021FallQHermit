# use Python 3
import socket
from sys import stdout
from time import time
from binascii import unhexlify
from datetime import datetime
ONE = 0.075
ZERO = 0.025

#varats code
def BinaryToDecimal(binary):
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return (decimal)

# enables debugging output
DEBUG = True
debugAVG = 0
debugCounter = 0
debugOneCounter = 0
debugZeroCounter = 0
debugOneAVG = 0
debugZeroAVG = 0
# set the server's IP address and port
#ip = "138.47.99.64"
ip = "localhost"
port = 1337

# create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
s.connect((ip, port))
covertBin = ""
# receive data until EOF
data = s.recv(4096).decode()
i = 0
covert = ""
while (data.rstrip("\n") != "EOF"):
	# output the data
	stdout.write(data)
	stdout.flush()
	# start the "timer", get more data, and end the "timer"
	t0 = time()
	data = s.recv(4096).decode()
	t1 = time()
	# calculate the time delta (and output if debugging)
	delta = round(t1 - t0, 3)
	#if delta > than the timing set for ONE, it be a one
	if delta >= ONE:
		covertBin += "1"
		if (DEBUG):
			debugOneCounter += 1
			debugOneAVG += delta
	#if not then zero
	else:
		covertBin += "0"
		if (DEBUG):
			debugZeroCounter += 1
			debugZeroAVG += delta
	#debug to get timing for all the things
	if (DEBUG):
		stdout.write(" {}\n".format(delta))
		stdout.flush()
		debugCounter += 1
		debugAVG += delta
	#when a full 8 bits are there
	if (len(covertBin) % 8 == 0):
		#take a slice 8 bits at a time
		#and convert to an ascii code
		b = int(covertBin[i:i + 8])
		n = int("0b{}".format(b), 2)
		#try to convert ascii code to ascii text
		try:
			covert += unhexlify("{0:x}".format(n)).decode("utf-8")

		except:
			covert += '?'
		if covert [-3:] == "EOF":
			covert = covert[:-3]
			break
		i += 8
# close the connection to the server
s.close()
#for some reason the print doesnt automatically go on a new line,
#hence the \n
print("\n{}".format(covertBin))
print("Time: {}".format(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")))
print(covert)
if (DEBUG):
	debugAVG = debugAVG/debugCounter
	debugOneAVG = debugOneAVG/debugOneCounter
	debugZeroAVG = debugZeroAVG/debugZeroCounter
	print("Average Delay of all of them: {}".format(debugAVG))
	print("Average Delay of ones: {}".format(debugOneAVG))
	print("Average Delay of zeroes: {}".format(debugZeroAVG))