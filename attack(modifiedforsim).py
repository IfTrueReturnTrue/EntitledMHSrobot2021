#!/usr/bin/eom ev3sim-micropython


from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor




import time


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


#Commence parts testing:
#define functions here
def defineObjectsAttack():
    #initialise motors (omni wheels)
    motor1 = MediumMotor(OUTPUT_A)
    motor2 = MediumMotor(OUTPUT_B)
    motor3 = MediumMotor(OUTPUT_C)
    motor4 = MediumMotor(OUTPUT_D)
    
    #init sensors
    
    ultrasonicFront = UltrasonicSensor(INPUT_2)
    ultrasonicLeft  = UltrasonicSensor(INPUT_3)
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
            pass
            
        
    except:
        pass

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
    
    

    