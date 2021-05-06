def defineObjectsAttack():
    movementMotor1 = LargeMotor(OUTPUT_A)
    movementMotor2 = LargeMotor(OUTPUT_B)
    punchMotor = MediumMotor(OUTPUT_C)
    touchSensor = TouchSensor(INPUT_1)

def defineObjectsDefend():
    movementMotor1 = LargeMotor(OUTPUT_A)
    movementMotor2 = LargeMotor(OUTPUT_B)
    collisionSensor = TouchSensor(INPUT_1)
    
    