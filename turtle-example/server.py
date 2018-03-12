# python2.7


from __future__ import unicode_literals
from __future__ import print_function

import socket
import turtle
import time
import sys

# from gpiozero import PWMOutputDevice
# from gpiozero import DigitalOutputDevice

# Setup constants from command line arguments
try:
    UDP_IP = sys.argv[1]
except IndexError:
    UDP_IP = "127.0.0.1"
try:
    UDP_PORT = sys.argv[2]
except IndexError:
    UDP_PORT = 2468
try:
    EXECUTION_SPEED_LIMIT = sys.argv[3]
except IndexError:
    EXECUTION_SPEED_LIMIT = 0.05


# -- Instructions definitions --
'''
This is the place where you define actions
for each instruction number (forward, down, left, right, ...)
'''


def forward():
    '''Instruction 1'''
    turtle.forward(4)


def back():
    '''Instruction 2'''
    turtle.back(5)


def right():
    '''Instruction 3'''
    turtle.right(8)


def left():
    '''Instruction 4'''
    turtle.left(8)


def stop():
    '''Instruction 5\n
    To set all controls to zero (off) state'''
    turtle.clear()

# -- End of instructions definitions --

# Dictionary with instructions
# bind to references of our command functions
instruction_set = {
    1: forward,
    2: back,
    3: right,
    4: left,
    5: stop,
}

# Setup listening UDP connection
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
print("Listening on {}:{}".format(UDP_IP, UDP_PORT))

# Main loop
while True:
    # Slow down the loop, gets buggy when too fast
    # You should try slowing down the remote first
    time.sleep(EXECUTION_SPEED_LIMIT)

    # Receive data from client ...
    data, addr = sock.recvfrom(8)

    # ... parse instruction ...
    message = int(data)

    # ... and execute it.
    instruction_set[message]()
