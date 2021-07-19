from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor
from ev3dev2.sensor import Sensor
import time
import threading




#Commence parts testing:
#define functions here
#APPEND: Assuming motor numbers based on clockwise position starting from true north 0^.
#APPEND: Assuming North and south motors are facing east. East and west motors are facing north.
motor1 = MediumMotor(OUTPUT_A)
motor2 = MediumMotor(OUTPUT_B)
motor3 = MediumMotor(OUTPUT_C)
motor4 = MediumMotor(OUTPUT_D)

#init sensors

ultrasonicFront = UltrasonicSensor(INPUT_2)
ultrasonicLeft  = UltrasonicSensor(INPUT_3)
    #initialise motors (omni wheels)

#S = SECONDS
#K = SPEED MULTIPLIER (-1 or 1)
#this function runs individual motors. Note that north and south motors are facing east, etc... Refer to #append at function definitions

'''
Note that the structure of the motors are like this:
            Motor 3: North

Motor 1: West          Motor 2 East


            Motor 4: South
'''
def runmotor(s, k, motor):
    try:
        if motor == "northmot":
            motor3.on_for_seconds(100 * k, s)
        elif motor == "southmot":
            motor4.on_for_seconds(100 * k, s)
        elif motor == "eastmot":
            motor2.on_for_seconds(100 * k, s)
        elif motor == "westmot":
            motor1.on_for_seconds(100 * k, s)
        else:
            pass
    except:
        print("Error, something happened.")
        pass

#this function moves the entire bot in one cardinal direction. Threading allows functions to run parallel to main code.
def movedir(s, direction):
    try:
        if direction == "north":
            threading.Thread(target=runmotor, args=(1, 1, "eastmot")).start()
            threading.Thread(target=runmotor, args=(1, 1, "westmot")).start()
        elif direction == "south":
            threading.Thread(target=runmotor, args=(1, -1, "eastmot")).start()
            threading.Thread(target=runmotor, args=(1, -1, "westmot")).start()
        elif direction == "east":
            threading.Thread(target=runmotor, args=(1, 1, "northmot")).start()
            threading.Thread(target=runmotor, args=(1, 1, "southmot")).start()
        elif direction == "west":
            threading.Thread(target=runmotor, args=(1, -1, "northmot")).start()
            threading.Thread(target=runmotor, args=(1, -1, "southmot")).start()
        else:
            pass


    except:
        print("Error, something happened.")
        pass


def sqrt(num):
    return num**0.5
somevalue = 0
def ultraSensingForMovement():

    errorAmount = 0
    forwardFB=ultrasonicFront.distance_centimeters
    sideFB=ultrasonicLeft.distance_centimeters
    calc1 = 1/sqrt(2)*sideFB #JUST SOME RECALCULATIONS TO THE CODE
    if (calc1 >= forwardFB - errorAmount) and calc1 <= forwardFB + errorAmount:
        print("There is a wall")
        return False
    else:
        print("There is a ball")
        return True
    '''oppCalc1 = sideFB/2
    oppCalc2 = forwardFB*(3/(sqrt(3)))
    if oppCalc1 - oppCalc2 < abs(errorAmount):

        print("There is a wall")
        return False
    else:

        print("There is a ball.")
        return True'''

while True:
    print("start")
    ultraSensingForMovement()
    if ultraSensingForMovement():
        movedir(1, "east")
    else:
        movedir(1, "north")
 #can edit this in if functions to match with ball sense.
                       #Though would not recommend as ball sense is still highly innacurate
    print("end")
    time.sleep(1)
