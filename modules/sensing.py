def touchSensing():
    if touchSensor.is_pressed() == True:
        return True
    else:
        return False

def ultraSensing():
    currentObjLocation = ultrasonic.distance_centimeters()
    currentTime = time()
    while time() -  currentTime <= 250:
        return
    else:
        newCurrentObjLocation = ultrasonic.distance_centimeters()
        if abs(newCurrentObjLocation - currentObjLocation) > #someValue:
            return True
        else:
            return False

