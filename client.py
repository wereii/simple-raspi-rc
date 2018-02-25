# python3

import sys
import socket
import keyboard
import time

# Nastaveni rychlosti snimani klaves v sekundach
zpozdeni = 0.1

# UDP_IP = input("Zadej IP (127.0.0.1): ") # Takhle by se po spusteni, python zeptal co chci priradit do promene UDP_IP
UDP_IP = "" # Takhle jsem prirovnal promene UDP_IP, hodnotu (textovy rezec aka string) "192.168..."
UDP_PORT = 6666 

if not UDP_IP:
	# Pokud neni zadana IP, nastav na localhost
	UDP_IP = "127.0.0.1"

if not UDP_PORT:
	# Pokud neni zadan port, nastav na 8008
	UDP_PORT = 8008

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Zpravy odesilam na {}:{}".format(UDP_IP, UDP_PORT))

def send_msg(data):
	# Kdyby se neco nepovedlo tak to chytame pomoci try
	try:
		sock.sendto(str(data).encode(), (UDP_IP, UDP_PORT))
	except Exception as ex:
		print("Zpravu se nepovedlo odeslat chyba: ")
		print(ex)

def try_is_pressed(key):
	try: 
		return keyboard.is_pressed(key)
	except RuntimeError:
		return False	

MESSAGE = ""
while True:
	time.sleep(zpozdeni)
		
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

# Aby se python hned neukoncil a mohli jsme se
# podivat co nam rika (pokud treba nastane chyba)
input()

	
