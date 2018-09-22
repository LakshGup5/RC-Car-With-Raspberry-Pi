print ("PROGRAM HAS RUN!")
import Ultrasonic
from evdev import InputDevice, categorize, ecodes
import RPi.GPIO as gpio
import time
#gpio.setwarnings(True)
gpio.setwarnings(False)
n1 = 7
n2 = 11     
n3 = 12
n4 = 13
n = [n1, n2, n3, n4]
gpio.setmode(gpio.BOARD)
gpio.setup(38, gpio.OUT)
motor = gpio.PWM(38, 100)
motor.start(0)
#creates object 'gamepad' to store the data
#you can call it whatever you like
switch = 310
up = 307
left = 304
right = 308
down = 305
d = 155
stopN = 311
m =38
auto = False
#fd()
#prints out device info at start
                


gamepad = InputDevice('/dev/input/event2')
#evdev takes care of polling the controller in a loop
skip = 0
skip2= 0
firstEvent=None
stop = True
while True:
    event = gamepad.read_one()
    if(event):
        print(event)
        stop = False
        if event.type == ecodes.EV_ABS:
            skip2+=1
            if(skip2 == 1):
                analog = categorize(event)
                axis = ecodes.bytype[analog.event.type][analog.event.code]
                value = analog.event.value
                if(axis == "ABS_Y"):
                    if(value == 0):
                        print("right")
                        Ultrasonic.rt()
                    if(value == 2):
                        print("left")
                        Ultrasonic.lt()
                if(axis == "ABS_X"):
                    if(value == 0):
                        print("up")
                        Ultrasonic.fd()
                    if(value == 2):
                        print("down")
                        Ultrasonic.bd()
            if(skip2 == 2):
                skip2 = 0
            
        elif event.type == ecodes.EV_KEY:
            print(event.code)
            skip+=1
            if(skip == 2):
                skip = 0
                if event.code == switch:
                    auto = not auto
                if(not auto):
                    if event.code == up:
                        print("up")
                        Ultrasonic.fd()
                    elif event.code == down:
                        print("down")
                        Ultrasonic.bd()
                    elif event.code == left:
                        print("left")
                        Ultrasonic.lt()
                    elif event.code == right:
                        print("right")
                        Ultrasonic.rt()
                    elif event.code == stopN:
                        print("stop")
                        Ultrasonic.stop()


    elif auto:
        Ultrasonic.mesure()


