def defineObjectsAttack():
    #make sure two large motors attached to output a and b
    driveMotor = MoveTank(OUTPUT_A, OUTPUT_B)
    #initialise gryosensor
    driveMotor.gyro = GyroSensor()
    tank.gryo.calibrate()
    #other sensors
    punchMotor = MediumMotor(OUTPUT_C)
    touchSensor = TouchSensor(INPUT_1)
    ultrasonic = UltrasonicSensor(INPUT_2)

def defineObjectsDefend():
    #make sure two large motors attached to output a and b
    driveMotor = MoveTank(OUTPUT_A, OUTPUT_B)
    
    collisionSensor = TouchSensor(INPUT_1)

    
    