from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
#from ev3dev2.sensor.lego import UltrasonicSensor, InfraredSensor #Disabled until installed on real robot

import time  
#Based on robot
motor1 = MediumMotor(OUTPUT_B)
motor2 = MediumMotor(OUTPUT_D)
motor3 = MediumMotor(OUTPUT_C)
motor4 = MediumMotor(OUTPUT_A)
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

while(True):
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
