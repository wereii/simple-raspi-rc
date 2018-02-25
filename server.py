# python2.7


from __future__ import unicode_literals
from __future__ import print_function

import socket
import turtle
import time
import sys
#from gpiozero import PWMOutputDevice
#from gpiozero import DigitalOutputDevice

# Setup constants from command line arguments
try:
    UDP_IP = sys.argv[1]
except IndexError:
    UDP_IP = "127.0.0.1"
try:
    UDP_PORT = sys.argv[2]
except IndexError:
    UDP_PORT = 8808
try:
    EXEC_SPEED_LIMITER = sys.argv[3]
except IndexError:
    EXEC_SPEED_LIMITER = 0.01


"""
Instructions definitions
This is the place where you define actions
for each instruction (ff, down, left, right, ...)
"""
def forward():
    # Instruction 1
    # turtle.forward(4)
    pass

def stop():
    # Instruction 5
    # set all controls to zero (off) state
    # turtle.clear()
    pass

def back():
    # Instruction 2
    # turtle.back(5)
    pass

def left():
    # Instruction 4
    # turtle.left(8)
    pass

def right():
    # Instruction 3
    # turtle.right(8)
    pass

# Dictionary with instructions \
# bind to references of our command functions
instruction_set = {
    1: forward,
    2: back,
    3: right,
    4: left,
    5: stop
}

# UDP connection setup
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Listening on {}:{}".format(UDP_IP, UDP_PORT))
sock.bind((UDP_IP, UDP_PORT))

# Main loop
while True:
	# Slow down the loop, gets buggy when too fast
	# You should try slowing down the client first
	time.sleep(EXEC_SPEED_LIMITER)

	# Receive data from client...
	data, addr = sock.recvfrom(8)
	
	# parse instruction...
	message = int(data)
	
	# and execute it.
	instruction_set[message]()

# Just for catching exceptions
input()
