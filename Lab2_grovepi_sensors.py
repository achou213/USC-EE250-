""" EE 250L Lab 02: GrovePi Sensors

No team members. I completed this lab on my own

Github repository link (with updated code): 
https://github.com/usc-ee250-spring2021/lab02-achou213.git
"""
import sys
import time
import grovepi
from grove_rgb_lcd import *

# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('../../Software/Python/')
# This append is to support importing the LCD library.
sys.path.append('../../Software/Python/grove_rgb_lcd')


# Connect the Grove Ultrasonic Ranger to digital port D4
# SIG,NC,VCC,GND
ultrasonic_ranger = 4
potentiometer = 0
grovepi.pinMode(potentiometer,"INPUT")
time.sleep(1)

# Full value of the rotary angle is 300 degrees, as per it's specs (0 to 300)
full_angle = 300
adc_ref = 5
grove_vcc = 5
count = 0
while True:
    

    # Read angle value from potentiometer
    sensor_value = grovepi.ultrasonicRead(ultrasonic_ranger)
    sensor_value2 = grovepi.analogRead(potentiometer)
    
    if sensor_value2 >= 517:
        sensor_value2 = 517
        
    if sensor_value < sensor_value2:
        setRGB(255,0,0)
        count = 1
        setText_norefresh("{:.0f}".format(sensor_value2) + "cm" + " OBJ PRES" + "\n%dcm" %sensor_value)
        time.sleep(0.2)
        
    elif (sensor_value > sensor_value2 & count == 1):
        setRGB(0,255,0)
        setText("{:.0f}".format(sensor_value2)+"cm\n%dcm" %sensor_value)
        time.sleep(0.2)
        count = 0
        
    else:
        setRGB(0,255,0)
        setText_norefresh("{:.0f}".format(sensor_value2)+"cm\n%dcm" %sensor_value)
        time.sleep(0.2)
    # Read distance value from Ultrasonic

   