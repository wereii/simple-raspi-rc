# python3

import sys
import socket
import keyboard
import time

DELAY = 0.1
UDP_IP = ""
UDP_PORT = 6666

if not UDP_IP:
    # Pokud neni zadana IP, nastav na localhost
    UDP_IP = "127.0.0.1"

if not UDP_PORT:
    # Pokud neni zadan port, nastav na 8008
    UDP_PORT = 8008

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

while True:
    time.sleep(DELAY)
    # Each command is presented as number
    # Server has definitions what to do for each number
    # It's possible to send whole word instead of number
    # but for sake of 

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

