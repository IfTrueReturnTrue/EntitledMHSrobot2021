def moveForwardUntilStopped():
    while go == True:
        try:
            movementMotor1.on_for_rotations(SpeedPercent(100), 3)
            movementMotor2.on_for_rotations(SpeedPercent(100), 3)
        except:
            ev3.screen.draw_text(40, 50, "Error! movement motor 1 not defined!")
            ev3.beep()
            break
    
    
    
    
    
    