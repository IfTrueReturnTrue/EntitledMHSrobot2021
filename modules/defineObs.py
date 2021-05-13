def defineObjectsAttack():
    #initialise motors (omni wheels)
    motor1 = MediumMotor(OUPUT_A)
    motor2 = MediumMotor(OUTPUT_B)
    motor3 = MediumMotor(OUTPUT_C)
    motor4 = MediumMotor(OUTPUT_D)
    #init sensors
    compass = CompassSensor(INPUT_3)
    
    ultrasonic = UltrasonicSensor(INPUT_2)

def defineObjectsDefend():
    #make sure two large motors attached to output a and b
    driveMotor = MoveTank(OUTPUT_A, OUTPUT_B)
    
    collisionSensor = TouchSensor(INPUT_1)

    
    