import RPi.GPIO as gpio
import time

# Initialize GPIO output pins
def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    gpio.setup(23, gpio.OUT)
    gpio.setup(24, gpio.OUT)

# Set all GPIO out to none
def stop():
    init()
    gpio.output(17,False)
    gpio.output(22, False)
    gpio.output(23,False)
    gpio.output(24, False)
    time.sleep(0.2)
    gpio.cleanup()

# Initialize GPIO pins for forward
def forward():
    init()
    gpio.output(17,True)
    gpio.output(22, False)
    gpio.output(23,True)
    gpio.output(24, False)

# Opposite GPIO pins from forward for output
def backward():
    init()
    gpio.output(17, False)
    gpio.output(22, True)
    gpio.output(23, False)
    gpio.output(24, True)

# Activate GPIO pins to turn right
def right():
    init()
    gpio.output(17, False)
    gpio.output(22, True)
    gpio.output(23, True)
    gpio.output(24, False)

# Reversed GPIO pins to turn left
def left():
    init()
    gpio.output(17, True)
    gpio.output(22, False)
    gpio.output(23, False)
    gpio.output(24, True)

