import math
import pygame as pg

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

def getDistance(a, b):

    return math.sqrt( (a[0] - b[0])**2 + (a[1] - b[1])**2 )

def getCenter(obj, size):

    return  obj.x + size[0]/2, obj.y + size[1]/2

def getBumper(obj, size, center):
  
    # print( obj.dirAngle)
    return center[0] + (size[1]/2)*math.cos(math.radians( obj.dirAngle)), center[1] - (size[1]/2)*math.sin(math.radians(obj.dirAngle))

def isValid(pos, maxS):

    if (pos[0] < 0 or pos[0] > maxS[0]) or (pos[1] < 0 or pos[1] > maxS[1]):
        return 0
    return 1

def isObstacle(color):

    th = 255*2
    if color[0] + color[1] + color[2] > th:
        return 1
    return 0

def findObstacle(screen, start, angle, screenSize):

    currPos = [start[0], start[1]]
    roundedCurrPos = [round(start[0]), round(start[1])]
    while isValid(currPos, screenSize):
        
        currCol = screen.get_at(roundedCurrPos)
        if isObstacle(currCol):
            break

        currPos[0] += math.cos(math.radians(angle))
        currPos[1] -= math.sin(math.radians(angle))
        roundedCurrPos = [ round(currPos[0]), round(currPos[1]) ]
    
    return currPos

def getFeatures(screen, car1, carSize, screenSize, show = 1):
    ##to draw the 5 lines out of the car
    carCenterPos = getCenter(car1, carSize) 
    carBumperPos = getBumper(car1, carSize, carCenterPos)
    
    #left horizontal line
    leftAngle = (car1.dirAngle + 90) % 360
    endPos1 = findObstacle(screen, carBumperPos, leftAngle, screenSize)
    leftDistance = getDistance(carBumperPos, endPos1)

    #left diagonal line
    leftDiagonalAngle = (car1.dirAngle + 45) % 360
    endPos2 = findObstacle(screen, carBumperPos, leftDiagonalAngle, screenSize)
    leftDiagonalDistance = getDistance(carBumperPos, endPos2)
   
    #straight line
    #gets obtacle, finds distance  and draws the line
    endPos3 = findObstacle(screen, carBumperPos, car1.dirAngle, screenSize)
    frontDistance = getDistance(carBumperPos, endPos3)
    
    #right diagonal line
    rightDiagonalAngle = (car1.dirAngle - 45) % 360
    endPos4 = findObstacle(screen, carBumperPos, rightDiagonalAngle, screenSize)
    rightDiagonalDistance = getDistance(carBumperPos, endPos4)
    
    #right horizontal line
    rightAngle = (car1.dirAngle - 90) % 360
    endPos5 = findObstacle(screen, carBumperPos, rightAngle, screenSize)
    rightDistance = getDistance(carBumperPos, endPos5)

    if show:
        pg.draw.line(screen, GREEN, carBumperPos, endPos1, 1)
        pg.draw.line(screen, GREEN, carBumperPos, endPos2, 1)
        pg.draw.line(screen, GREEN, carBumperPos, endPos3, 1)
        pg.draw.line(screen, GREEN, carBumperPos, endPos4, 1)
        pg.draw.line(screen, GREEN, carBumperPos, endPos5, 1)
    return [ leftDistance, leftDiagonalDistance, frontDistance, rightDiagonalDistance, rightDistance, car1.speed, car1.abPedal, car1.stAngle ]
