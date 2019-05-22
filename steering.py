import math

#follows cartesian system
#iDirAngle - Initial movement angle
#iSpeedX - Initial Speed along X 
#iSpeedY - Inital Speed along Y (|speed| < Limit? )
#abPedal - Acceleration and Break Pedal (-5 to +4)
#stAngle - Steering Angle (-60 to 60)

#Globals

NORM = 3
abMAX = 4
speedMAX = 50;
# timeInterval = 0.1 seconds by default

def getTotalSpeed(xSpeed, ySpeed):
    return math.sqrt( xSpeed**2 + ySpeed**2 )

def getAcDc(multiplier):
    return multiplier*abMAX

def addSpeeds(a, b):

    toReturn = a + b
    if toReturn > speedMAX:
        return speedMAX
    elif toReturn < 0:
        return 0
    else:
        return toReturn

def sgn(x):
    
    if (x == 0):
        return 0
    else:
        return x/abs(x)

def getSpeedComps(spd, theta):
    
    return spd * math.cos( math.radians(theta) ), spd * math.sin( math.radians(theta) )

def getNewSpeed(iDirAngle, iSpeedX, iSpeedY, abPedal, stAngle, timeInterval = 0.1):

    acc = getAcDc(abPedal)
    
    deltaSpeed = acc * timeInterval / NORM
    oldSpeed = getTotalSpeed(iSpeedX, iSpeedY)
    newSpeed = addSpeeds(oldSpeed, deltaSpeed)
    
    turnDirection = sgn(stAngle)
    # perpAngle = ( iDirAngle + (turnDirection * 90) ) % 360 #angle perp to iDirAngle
    
    newDirAngle = iDirAngle - (stAngle/NORM)
    newSpeedX, newSpeedY = getSpeedComps(newSpeed, newDirAngle)
    
    return newDirAngle, newSpeedX, newSpeedY

def rotateCenter(obj, rotatedImage):

    r = rotatedImage.get_rect().center

    return obj.x  - r[0], obj.y - r[1]
