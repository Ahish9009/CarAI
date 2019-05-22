import pygame as pg
import numpy as np
import steering as st

pg.init()

#global variables
#--------------------------------------------

#text
TNR30 = pg.font.SysFont("Times New Roman", 30)

#colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

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
car = pg.image.load("images/car.png")
circuit = pg.image.load("images/circuit.png")

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

#dummy car
car1 = cars()
orgCar = car

oldT = pg.time.get_ticks()

while looper:
    
    #gets the text to print
    abInfo = TNR30.render("abPedal: "+str(car1.abPedal), 1, BLACK)
    SpeedInfo = TNR30.render("Speed: "+str(car1.speed), 1, BLACK)
    stInfo = TNR30.render("Steering Angle: "+str(car1.stAngle), 1, BLACK)
    fps = TNR30.render(f"{ clock.get_fps() }FPS", 1, BLACK)
   
    #rotates the original image of the car
    car = orgCar
    car = pg.transform.rotate(car, car1.dirAngle-90)
    
    #blits images
    screen.blit(circuit, (0,0))
    screen.blit(car, st.rotateCenter(car1, car))

    #blits text
    screen.blit(abInfo, (0,30))
    screen.blit(SpeedInfo, (0,65))
    screen.blit(stInfo, (0, 100))
    screen.blit(fps, (0, 575))

    # car1.abPedal = 1
    # car1.stAngle = -6
    # car1.xSpeed = 0.5
    # car1.ySpeed = 0.5

    for event in pg.event.get():

        if event.type == pg.QUIT:
            looper = False

        if event.type == pg.KEYDOWN:

            if event.key == pg.K_UP:
                car1.abPedal += 0.5
            if event.key == pg.K_DOWN:
                car1.abPedal -= 0.5
            if event.key == pg.K_RIGHT:
                car1.stAngle += 1
            if event.key == pg.K_LEFT:
                car1.stAngle -= 1

    #sets max framerate
    clock.tick(10)
    
    #updates the car's position
    currT = pg.time.get_ticks()
    deltaT = (currT - oldT)/1000
    # print(deltaT)
    # print(car1.x, car1.y)
    car1.updatePos(deltaT)
    oldT = pg.time.get_ticks()
    
    pg.display.update()

pg.quit()





