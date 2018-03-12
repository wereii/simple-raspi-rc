# simple-raspi-rc
This is simple script written for remote control of raspberry pi's GPIO over UDP (within local subnet, eg. wifi)

It's intent is to control the raspberrypi motors over gpio but it can be easily forged to do anything else.

### Installation
On remote (your computer): 
- Download python3.6
- Execute in command line: `pip install keyboard`
- Run `remote.py` with root/admin privileges. ( `keyboard` module needs admin priv.)

On server (RaspberryPi):
- Setup what should the Raspberry do for each instruction in `Instructions definitions` in `server.py`
- Just run it (with python2.7)

### Notes
You should be able to run the files on both python2 and 3 but I have had to run `server.py` with python2.7 on RaspberryPi as the gpiozero wasn't working with python3, `remote.py` is intended to run on python3.6.
Instructions are sent as numbers (starting with 1). 
I am not really sure about decoding/encoding part, that could be done probably better.
