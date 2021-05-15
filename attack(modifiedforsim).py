#!/usr/bin/eom ev3sim-micropython


from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor




import time





#Commence parts testing:
#define functions here
motor1 = MediumMotor(OUTPUT_A)
motor2 = MediumMotor(OUTPUT_B)
motor3 = MediumMotor(OUTPUT_C)
motor4 = MediumMotor(OUTPUT_D)

#init sensors

ultrasonicFront = UltrasonicSensor(INPUT_2)
ultrasonicLeft  = UltrasonicSensor(INPUT_3)
    #initialise motors (omni wheels)
    
#SPEED between 0, 100
def moveatspeedindir(s, dir):
    try:
        rot = 1
        if dir == "left":
            motor3.on_for_rotations(s,  rot)#here rot is only a placeholder.
            motor4.on_for_rotations(s,  rot)
        elif dir == "right":
            motor3.on_for_rotations(s,  -rot)  #negative rot for opposite to normal
            motor4.on_for_rotations(s,  -rot)  
        elif dir == "up":
            motor1.on_for_rotations(s,  rot)
            motor2.on_for_rotations(s,  rot)
        elif dir == "down":
            motor1.on_for_rotations(s,  -rot)  
            motor2.on_for_rotations(s,  -rot)
        else:
            pass
            
        
    except:
        print("Error, something happened.")
        pass

def sqrt(num):
    return num**0.5
somevalue = 0
def ultraSensingForMovement():

    errorAmount =3
    forwardFB=ultrasonicFront.distance_centimeters
    sideFB=ultrasonicLeft.distance_centimeters
    oppCalc1 = sideFB/2
    oppCalc2 = forwardFB*(3/(sqrt(3)))
    if oppCalc1 - oppCalc2 < abs(errorAmount):
        
        print("There is a wall")
        return False
    else:
        
        print("There is a ball.")
        return True


    
    





print("yes") #test if everything is working (no syntatical errors)

ultraSensingForMovement() # initial test
if ultraSensingForMovement():
    #5 is just an arbritrary number below. 
    for x in range(5): #This just repeats the movement 5 times
        moveatspeedindir(100, "right")
time.sleep(1)



    