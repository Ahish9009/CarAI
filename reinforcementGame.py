import pygame as pg
import numpy as np
import steering as st
import obstacles as ob
# import autoPilot as ap
# import autoPilot2 as ap2
# import autoPilot3 as ap3
# import tfAutoPilot as tfap
import reinforcementFunctions as rf
import math, csv

pg.init()
#-------------------------------------------
nFeatures = 10
#-------------------------------------------
#global variables
#--------------------------------------------
#starting positions
#circuit1 - 400,150
#circuit2 - 50, 200
#circuit3 - 50, 125 
#circuit4 - 200,200
startPos = [(400,150), (50,200), (50,125), (200,200)]

#text
TNR30 = pg.font.SysFont("Times New Roman", 30)

#colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#sizes
screenSize = (600,600)
carSize = (30,60) #when car is facing upwards

class cars:

    def __init__(self, xInit = 100 + carSize[0], yInit = 100 + carSize[1]):

        #initial positions of the car
        self.x = xInit
        self.y = yInit

        #initial parameters of the car
        self.distance = 0
        self.abPedal = 0
        self.speed = 0
        self.xSpeed = 0
        self.ySpeed = 0
        self.dirAngle = 90 #car is facing upwards
        self.stAngle = 0

    def updatePos(self, timeInterval = 0.1):

        #ugly code - passing all object parameters instead of just object
        self.dirAngle, self.xSpeed, self.ySpeed = st.getNewSpeed(self.dirAngle, self.xSpeed, self.ySpeed, self.abPedal, self.stAngle, timeInterval)
        
        self.speed = st.getTotalSpeed(self.xSpeed, self.ySpeed)
        self.x += self.xSpeed * timeInterval
        self.y -= self.ySpeed * timeInterval
        self.distance += (self.speed*timeInterval)

#loading the images
car = pg.image.load("images/rfCar.png")
leadingCar = pg.image.load("images/leadCar.png")
circuit1 = pg.image.load("images/circuit1.png")
circuit2 = pg.image.load("images/circuit2.png")
circuit3 = pg.image.load("images/circuit3.png")
circuit4 = pg.image.load("images/circuit4.png")

#scaling the images
circuit1 = pg.transform.scale(circuit1, screenSize)
circuit2 = pg.transform.scale(circuit2, screenSize)
circuit3 = pg.transform.scale(circuit3, screenSize)
circuit4 = pg.transform.scale(circuit4, screenSize)
car = pg.transform.scale(car, carSize)
leadingCar = pg.transform.scale(leadingCar, carSize)

currCircuit = 2
circuits = [circuit1, circuit2, circuit3, circuit4]
circuit = circuits[currCircuit]

#frame rate
clock = pg.time.Clock()

#starts the screen
screen = pg.display.set_mode(screenSize)
pg.display.set_caption("CarAI")

#pg loop
looper = True
count = 0

#No. of cars to try
m = 300

#starting randomized values
deltaAb = 0.05
deltaSt = 0.5
abPedalWeights = rf.getRandom(m, nFeatures, deltaAb)
stAngleWeights = rf.getRandom(m, nFeatures, deltaSt)

print(abPedalWeights)
print()
print(stAngleWeights)

#car objects list
carsList = [cars(*startPos[currCircuit]) for i in range(m)]
alive = [1 for i in range(m)]

#car image
orgCar = car
orgLeadingCar = leadingCar

oldT = pg.time.get_ticks()

autoPilot = True

nGenerations = 0
triggerNextGen = False

while looper:
    
    #blits images
    screen.blit(circuit, (0,0))
 
    if triggerNextGen:

        currCircuit = (currCircuit + 1) % 4
        circuit = circuits[currCircuit]
        screen.blit(circuit, (0,0))

        nGenerations += 1

        carsList = [cars(*startPos[currCircuit]) for i in range(m)]
        alive = [1 for i in range(m)]

        leadAbPedalWeights = abPedalWeights[lead-1]
        leadStAngleWeights = stAngleWeights[lead-1]
        print(leadAbPedalWeights)
        print(leadStAngleWeights)
        print()

        # nextDeltaAb = np.average(leadAbPedalWeights)
        # nextDeltaSt = np.average(leadStAngleWeights)
        nextDeltaAb = deltaAb*0.4
        nextDeltaSt = deltaSt*0.4
        abPedalWeights = rf.getNextRandom(leadAbPedalWeights, nextDeltaAb, m, nFeatures)
        stAngleWeights = rf.getNextRandom(leadStAngleWeights, nextDeltaSt, m, nFeatures)

        triggerNextGen = False

    if autoPilot:
        #updates alive cars
        newCrashed = rf.getCrashStatus(carsList, screen, screenSize, carSize, alive)
        alive = list(map(lambda x, new: 1 if x and new else 0, alive, newCrashed))
        nAlive = alive.count(1)

        #blits cars alive
        aliveInfo = TNR30.render("Alive: "+str(nAlive), 1, BLACK)
        generationsInfo = TNR30.render("Generation: "+str(nGenerations), 1, BLACK)
        screen.blit(aliveInfo, (0,30))
        screen.blit(generationsInfo, (0,65))

        #gets cars to show
        carsBlitList = list(map(lambda x, y: x if y else False, carsList, alive))

        #gets new abPedal & stAngle for all cars
        carsList = rf.driveAll(carsList, abPedalWeights, stAngleWeights, screen, carSize, screenSize)

        for currCar in filter(lambda x: x!=False, carsBlitList):
            car = pg.transform.rotate(car, currCar.dirAngle-90)
            screen.blit(car, st.rotateCenter(currCar, car))
            car = orgCar #resets car image to original(continous rotation causes distortion)
        
        #gets leading car
        info = list(map(lambda x, i: (x.distance,i), carsList, range(1,m+1)))
        info.sort(key=lambda x:x[0])
        lead = info[-1][1]
        speedInfo = TNR30.render("Speed: "+str(carsList[lead-1].speed), 1, BLACK)
        abInfo = TNR30.render("ab: "+str(carsList[lead-1].abPedal), 1, BLACK)
        stInfo = TNR30.render("st: "+str(carsList[lead-1].stAngle), 1, BLACK)
        screen.blit(speedInfo, (0,100))
        screen.blit(abInfo, (0,135))
        screen.blit(stInfo, (0,170))

        #blits leading car
        leadingCar = pg.transform.rotate(leadingCar, carsList[lead-1].dirAngle-90)
        screen.blit(leadingCar, st.rotateCenter(carsList[lead-1], leadingCar))
        leadingCar = orgLeadingCar
        
        # gets new abPedal & stAngle for all cars
        # carsList = rf.driveAll(carsList, abPedalWeights, stAngleWeights, screen, carSize, screenSize)
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            looper = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_a:
                autoPilot = not autoPilot
            if event.key == pg.K_n:
                triggerNextGen = True

    #sets max framerate
    clock.tick(20)

    currT = pg.time.get_ticks()
    deltaT = (currT - oldT)/1000

    if autoPilot:
        for i in range(m):
            if alive[i]:
                carsList[i].updatePos()

    oldT = pg.time.get_ticks()
    
    pg.display.update()

pg.quit()


