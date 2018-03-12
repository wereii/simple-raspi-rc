# python3

import sys
import socket
import keyboard
import time

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
    EXECUTION_SPEED_LIMIT = 0.1

# Prepare UDP connection to server
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Sending commands to {}:{}".format(UDP_IP, UDP_PORT))


def send_msg(data):
    try:
        sock.sendto(str(data).encode(), (UDP_IP, UDP_PORT))
    except Exception as ex:
        print("Something went wrong.")
        print(ex)


def try_is_pressed(key):
    # Catching 'dictionary changed size'
    try:
        return keyboard.is_pressed(key)
    except RuntimeError:
        return False

# Main loop
while True:
    # Wait some time
    # Gets buggy if too low
    time.sleep(EXECUTION_SPEED_LIMIT)

    if try_is_pressed('up'):
        send_msg(1)

    if try_is_pressed('down'):
        send_msg(2)

    if try_is_pressed('right'):
        send_msg(3)

    if try_is_pressed('left'):
        send_msg(4)

    if try_is_pressed('esc'):
        send_msg(5)
