from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
import InfraredSensor #no clue where this is
#from ev3dev2.sensor.lego import UltrasonicSensor, InfraredSensor #Disabled until installed on real robot

import time  
import math
#Based on robot
motor1 = MediumMotor(OUTPUT_B)
motor2 = MediumMotor(OUTPUT_D)
motor3 = MediumMotor(OUTPUT_C)
motor4 = MediumMotor(OUTPUT_A)
infrared = InfraredSensor(INPUT_1)
"""  Disabled until installed on real robot
infrared = InfraredSensor(INPUT_2)
ultrasonicFront  = UltrasonicSensor(INPUT_3)
ultrosonicLeft = UltrasonicSensor(INPUT_4)
"""
def movement(direction, rotations):
    if(direction == "North"):
        motor2.on_for_rotations(-100, rotations, block=False)
        motor4.on_for_rotations(100, rotations, block=False)
    if(direction == "East"):
        motor1.on_for_rotations(100, rotations, block=False)
        motor3.on_for_rotations(-100, rotations, block=False)
    if(direction == "South"):
        motor2.on_for_rotations(100, rotations, block=False)
        motor4.on_for_rotations(-100, rotations, block=False)
    if(direction == "West"):
        motor1.on_for_rotations(-100, rotations, block=False)
        motor3.on_for_rotations(100, rotations, block=False)

def motorsOff():
    motor1.off()
    motor2.off()
    motor3.off()   
    motor4.off()

class Vector2:
    def __init__(self, radius,  angle):
        self.x_component =  radius * math.cos(angle)
        self.y_component = radius * math.sin(angle)
    def get_components(self):
        return self.x_component, self.y_component
def detect_ball():
    
    
    if infrared.beacon():
        vector = Vector2(infrared.beacon()[0], infrared.beacon()[1])
    else:
        return False
    

while(True):
    if detect_ball():

        try: 
            movement("North", 100)
            movement("East", 100)
            time.sleep(2)
            motorsOff()
            movement("South", 100)
            movement("West", 100)
            time.sleep(2)
            motorsOff()
        except KeyboardInterrupt as error:
            motor1.off()
            motor2.off()
            motor3.off()    
            motor4.off()
            raise error
    else:
        try:
            print("There is no ball detected")
        except:
            raise error
