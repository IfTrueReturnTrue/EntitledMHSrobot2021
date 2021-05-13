#!/usr/bin/env pybricks-micropython
from EntitledMHSrobot2021.modules.defineObs import defineObjectsAttack
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor, CompassSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


import time
#importing homemade modules
from modules.defineObs import *
from modules.movement import *
from modules.sensing import *
import time

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()



# Write your program here.
ev3.speaker.beep()

#Commence parts testing:
defineObjectsAttack()
while True:
    foo = 0
    print("yes")
    #make it point in direction of the opponent's goal
    driveMotor.turn_degrees(foo)
    ultraSensing()
    
    

    