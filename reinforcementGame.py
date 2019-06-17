import pygame as pg
import numpy as np
import steering as st
import obstacles as ob
import autoPilot as ap
import autoPilot2 as ap2
import autoPilot3 as ap3
import tfAutoPilot as tfap
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

#stores all collected features
allFeatures = []

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
        self.abPedal = 0
        self.speed = 0
        self.xSpeed = 0
        self.ySpeed = 0
        self.dirAngle = 90 #car is facing upwards
        self.stAngle = 0

    def updatePos(self, timeInterval = 0.1):

        self.dirAngle, self.xSpeed, self.ySpeed = st.getNewSpeed(self.dirAngle, self.xSpeed, self.ySpeed, self.abPedal, self.stAngle, timeInterval)
        
        self.speed = st.getTotalSpeed(self.xSpeed, self.ySpeed)
        self.x += self.xSpeed * timeInterval
        self.y -= self.ySpeed * timeInterval

#loading the images
car = pg.image.load("images/rfCar.png")
circuit = pg.image.load("images/circuit4.png")

#scaling the images
circuit = pg.transform.scale(circuit, screenSize)
car = pg.transform.scale(car, carSize)

#frame rate
clock = pg.time.Clock()

#starts the screen
screen = pg.display.set_mode(screenSize)
pg.display.set_caption("CarAI")

#pg loop
looper = True
count = 0

#No. of cars to try
m = 600
carsList = []

#starting randomized values
delta = 1
abPedalWeights = rf.getRandom(m, nFeatures, delta)
stAngleWeights = rf.getRandom(m, nFeatures, delta)

#car objects list
carsList = [cars(200,200) for i in range(m)]
alive = [1 for i in range(m)]

#car image
orgCar = car

oldT = pg.time.get_ticks()

autoPilot = False

while looper:
    
    #blits images
    screen.blit(circuit, (0,0))
   
    #updates alive cars
    newCrashed = rf.getCrashStatus(carsList, screen, screenSize, carSize)
    alive = list(map(lambda x, new: 1 if x and (new) else 0, alive, newCrashed))
    nAlive = alive.count(1)

    aliveInfo = TNR30.render("Alive: "+str(nAlive), 1, BLACK)
    screen.blit(aliveInfo, (0,30))

    carsBlitList = list(map(lambda x, y: x if y else False, carsList,alive ))

    for currCar in filter(lambda x: x!=False, carsBlitList):
        car = pg.transform.rotate(car, currCar.dirAngle-90)
        # print(currCar.x, currCar.y)
        screen.blit(car, st.rotateCenter(currCar, car))
        car = orgCar #resets car image to original(continous rotation causes distortion)
    
    carsList = rf.driveAll(carsList, abPedalWeights, stAngleWeights, screen, carSize, screenSize)
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            looper = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_a:
                autoPilot = not autoPilot

    #sets max framerate
    clock.tick(10)

    #updates the car's position
    currT = pg.time.get_ticks()
    deltaT = (currT - oldT)/1000

    for i in range(m):
        carsList[i].updatePos()

    oldT = pg.time.get_ticks()

    
    pg.display.update()

pg.quit()


