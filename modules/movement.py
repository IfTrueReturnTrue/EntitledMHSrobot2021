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
            ev3.screen.draw_text(40, 50, "Input into function was not valid!")
            ev3.beep()
            
        
    except:
        ev3.screen.draw_text(40, 50, "Error! Something went wrong!")
        ev3.beep()




        
    
    
    
    
    
    