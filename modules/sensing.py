'''
def touchSensing():
    return touchSensor.is_pressed()
    
somevalue = 0
def ultraSensingForMovement():
    currentObjLocation = ultrasonic.distance_centimeters()
    currentTime = time()
    while time() -  currentTime <= 250:
        return
    else:
        newCurrentObjLocation = ultrasonic.distance_centimeters()
        if abs(newCurrentObjLocation - currentObjLocation) > somevalue:
            return True
        else:
            return False
def ultraSensingForStill():
    currentObjDistance = ultrasonic.distance_centimeters()
    
'''  


