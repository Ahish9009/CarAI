import math

#follows cartesian system
#iDirAngle - Initial movement angle
#iSpeedX - Initial Speed along X 
#iSpeedY - Inital Speed along Y (|speed| < Limit? )
#abPedal - Acceleration and Break Pedal (-5 to +4)
#stAngle - Steering Angle (-60 to 60)

#Globals

abMAX = 4
speedMAX = 50;
timeInterval = 0.1 #seconds

def getTotalSpeed(xSpeed, ySpeed):
    return math.sqrt( xSpeed**2 + ySpeed**2 )

def getAcDc(multiplier):
    return multiplier*abMAX

def addSpeeds(a, b):

    toReturn = a + b
    if toReturn > speedMAX:
        return speedMAX
    else if toReturn < 0:
        return 0
    else:
        return toReturn

def sgn(x):
    
    if (x == 0):
        return 0
    else:
        return x/abs(x)

def getNewSpeed(iDirAngle, iSpeedX, iSpeedY, abPedal, stAngle):

    acc = getAcDc(abPedal)
    
    deltaSpeed = acc*timeInterval
    oldSpeed = getTotalSpeed(iSpeedX, iSpeedY)
    newSpeed = addSpeeds(oldSpeed, deltaSpeed)
    
    turnDirection = sgn(stAngle)
    perpAngle = ( iDirAngle + (turnDirection*90) ) % 360
    

    return (x,y)
