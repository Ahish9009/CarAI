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
# model = "tensorFlow"
model = "test"
nFeatures = 10
#-------------------------------------------

#global variables
#--------------------------------------------

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
circuit = pg.image.load("images/circuit4.png")

#scaling the images
circuit = pg.transform.scale(circuit, screenSize)
car = pg.transform.scale(car, carSize)
leadingCar = pg.transform.scale(leadingCar, carSize)

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
delta = 0.5
abPedalWeights = rf.getRandom(m, nFeatures, delta)
stAngleWeights = rf.getRandom(m, nFeatures, delta)

print(abPedalWeights)
print()
print(stAngleWeights)

#car objects list
carsList = [cars(200,200) for i in range(m)]
alive = [1 for i in range(m)]

#car image
orgCar = car
orgLeadingCar = leadingCar

oldT = pg.time.get_ticks()

autoPilot = True

while looper:
    
    #blits images
    screen.blit(circuit, (0,0))
  
    if not autoPilot:
        info = list(map(lambda x, i: (x.distance,i), carsList, range(1,m+1)))
        info.sort(key=lambda x:x[0])
        print(info)
        with open("reinforcement/abWeights", "a", newline='') as f:
            csvWriter = csv.writer(f, delimiter = ',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for i in abPedalWeights:
                csvWriter.writerow(i)

        with open("reinforcement/stWeights", "a", newline='') as f:
            csvWriter = csv.writer(f, delimiter = ',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for i in stAngleWeights:
                csvWriter.writerow(i)

        input()
        #----------------------------------------------------------------------

    if autoPilot:
        #updates alive cars
        newCrashed = rf.getCrashStatus(carsList, screen, screenSize, carSize, alive)
        alive = list(map(lambda x, new: 1 if x and (new) else 0, alive, newCrashed))
        nAlive = alive.count(1)

        #blits cars alive
        aliveInfo = TNR30.render("Alive: "+str(nAlive), 1, BLACK)
        screen.blit(aliveInfo, (0,30))

        #gets cars to show
        carsBlitList = list(map(lambda x, y: x if y else False, carsList, alive))

        for currCar in filter(lambda x: x!=False, carsBlitList):
            car = pg.transform.rotate(car, currCar.dirAngle-90)
            # print(currCar.x, currCar.y)
            screen.blit(car, st.rotateCenter(currCar, car))
            car = orgCar #resets car image to original(continous rotation causes distortion)
        
        #gets leading car
        info = list(map(lambda x, i: (x.distance,i), carsList, range(1,m+1)))
        info.sort(key=lambda x:x[0])
        lead = info[-1][1]

        #blits leading car
        leadingCar = pg.transform.rotate(leadingCar, carsList[lead-1].dirAngle-90)
        screen.blit(leadingCar, st.rotateCenter(carsList[lead-1], leadingCar))
        leadingCar = orgLeadingCar
        
        #gets new abPedal & stAngle for all cars
        carsList = rf.driveAll(carsList, abPedalWeights, stAngleWeights, screen, carSize, screenSize)
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            looper = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_a:
                autoPilot = not autoPilot

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


