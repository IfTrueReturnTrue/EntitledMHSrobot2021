#!/usr/bin/env pybricks-micropython
'''
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor, CompassSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


import time


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()



# Write your program here.
ev3.speaker.beep()

#Commence parts testing:
#define functions here
def defineObjectsAttack():
    #initialise motors (omni wheels)
    motor1 = MediumMotor("outA")
    motor2 = MediumMotor("outC")
    motor3 = MediumMotor("outB")
    motor4 = MediumMotor("outD")
    
    #init sensors
    compass = CompassSensor("in1")
    ultrasonicFront = UltrasonicSensor("in2")
    ultrasonicLeft  = UltrasonicSensor("in3")
#SPEED between 0, 100
def moveAtSpeedinDir(s, dir):
    try:
        rot = 3
        if dir == "left":
            motor2.on_for_rotations(s,  rot)#here   rot is only a placeholder.
            motor4.on_for_rotations(s,  rot)#negative   rot for opposite to normal
        elif dir == "right":
            motor2.on_for_rotations(s,  rot)
            motor4.on_for_rotations(s,  rot)  
        elif dir == "up":
            motor1.on_for_rotations(s,  rot)
            motor3.on_for_rotations(s,  rot)
        elif dir == "down":
            motor1.on_for_rotations(s,  rot)  
            motor3.on_for_rotations(s,  rot)
        else:
            ev3.screen.draw_text(40, 50, "Input into function was not valid!")
            ev3.beep()
            
        
    except:
        ev3.screen.draw_text(40, 50, "Error! Something went wrong!")
        ev3.beep()

def sqrt(num):
    return num**0.5
somevalue = 0
def ultraSensingForMovement():
    errorAmount = 3
    forwardFB=ultrasonicFront.distance_centimeters()
    sideFB=ultrasonicLeft.distance_centimeters()
    oppCalc1 = sideFB/2
    oppCalc2 = forwardFB*(3/(sqrt(3)))
    if oppCalc1 - oppCalc2 < abs(errorAmount):
        return False
        print("There is a wall")
    else:
        return True
        print("There is a ball.")

    
    


defineObjectsAttack()
while True:
    foo = 0
    print("yes")
    #make it point in direction of the opponent's goal
    
    time.sleep(1)
'''
    

    