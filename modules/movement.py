#SPEED between 0, 100
def moveAtSpeed(speed):
    try:

        driveMotor.on_for_rotations(speed, speed, 3 )#variable '3' only placeholder
        
    except:
        ev3.screen.draw_text(40, 50, "Error! movement motor 1 not defined!")
        ev3.beep()


def turnSetDegrees(amount, direction):
    try:
        if direction == "left":

            driveMotor.turn_left(100, amount)
        else:
            driveMotor.turn_right(100, amount)
    except:
        ev3.screen.draw_text(40, 50, "Error! Something went wrong!")
        ev3.beep()



        
    
    
    
    
    
    