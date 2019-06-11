import math
import pygame as pg
import numpy as np

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

def sgn(x):

    if x == 0:
        return 0
    return x/abs(x)

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
    roundedCurrPos = [int(round(start[0])), int(round(start[1]))]
    while isValid(currPos, screenSize):
        
        currCol = screen.get_at(roundedCurrPos)
        if isObstacle(currCol):
            break

        currPos[0] += math.cos(math.radians(angle))
        currPos[1] -= math.sin(math.radians(angle))
        roundedCurrPos = [ int(round(currPos[0])), int(round(currPos[1])) ]
    
    return currPos


def getNdistances(screen, car, carSize, screenSize, show=1, n=7):
    carCenterPos = getCenter(car, carSize)
    carBumperPos = getBumper(car, carSize, carCenterPos)

    # Asserting min 3 distances: left, right, front
    assert n >= 3

    # if n is odd, it will contain the straight line else, it won't
    angles = (np.linspace(-90, 90, n) + car.dirAngle) % 360
    # with the angles, find the end position
    endPos = list(map(lambda angle: findObstacle(screen, carBumperPos, angle, screenSize), angles))
    # using the end position [nearest obstacle], calculate the distance
    n_distances = list(map(lambda pos: getDistance(carBumperPos, pos), endPos))

    if show:
        # draw the lines
        for pos in endPos:
            pg.draw.line(screen, GREEN, carBumperPos, pos, 1)

    return n_distances


def get5Features(screen, car1, carSize, screenSize, show=1):
    return [ *getNdistances(screen, car1, carSize, screenSize, n=5), car1.speed, car1.abPedal, car1.stAngle ]


def get7Features(screen, car1, carSize, screenSize, show=1):
    return [ *getNdistances(screen, car1, carSize, screenSize, n=7), car1.speed, car1.abPedal, car1.stAngle ]


def get11Features(screen, car1, carSize, screenSize, show=1):
    direction = sgn(car1.dirAngle)

    return [ *getNdistances(screen, car1, carSize, screenSize, n=9), car1.speed, direction, car1.abPedal, car1.stAngle ]

