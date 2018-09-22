print("OTHER PROGRAM HAS RUN!")
import RPi.GPIO as gpio
gpio.setmode(gpio.BOARD)
import time
import random
true = True
false = False
gpio.setwarnings(false)
trig = 40
echo = 15
n1 = 7
n2 = 11
n3 = 12
n4 = 13
enA = 16
enB = 18
n = [n1, n2, n3, n4,enA,enB]
gpio.setmode(gpio.BOARD)
gpio.setup(n, gpio.OUT)
gpio.output(enA,True)
gpio.output(enB,True)
def stop():
    gpio.output(n1, False)
    gpio.output(n2, False)
    gpio.output(n3, False)
    gpio.output(n4, False)
def fd():
    gpio.output(n1, False)
    gpio.output(n2, True)
    gpio.output(n3, True)
    gpio.output(n4, False)
def bd():
    gpio.output(n1, True)
    gpio.output(n2, False)
    gpio.output(n3, False)
    gpio.output(n4, True)
def rt():
    gpio.output(n1, True)
    gpio.output(n2, False)
    gpio.output(n3, True)
    gpio.output(n4, False)
def lt():
    gpio.output(n1, False)
    gpio.output(n2, True)
    gpio.output(n3, False)
    gpio.output(n4, True)

gpio.setup(trig, gpio.OUT)
gpio.setup(echo, gpio.IN)
def mesure():
    #gpio.output(trig, false)
    #time.sleep(0.05)
    gpio.output(trig, true)
    time.sleep(0.05)
    gpio.output(trig, false)
    while (gpio.input(echo)) == 0:
        start = time.time()
    while (gpio.input(echo)) == 1:
        end = time.time()
    dur = end-start
    dis = dur*17150
    print (dis)
    chooser = random.randint(0, 1) 
    if dis <= 10:
        if chooser == 1:
            lt()
            time.sleep(5)
        else:
            rt()
            time.sleep(5)
    else:
        fd()
