import math

def getDistance(a, b):

    return math.sqrt( (a[0] - b[0])**2 + (a[1] - b[1])**2 )

def getCenter(obj, size):

    return obj.x + size[0]/2, obj.y + size[1]/2

def getBumper(obj, size, center):
  
    # print(obj.dirAngle)
    return center[0] + (size[1]/2)*math.cos(math.radians(obj.dirAngle)), center[1] - (size[1]/2)*math.sin(math.radians(obj.dirAngle))

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


