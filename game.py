import pygame as pg
import numpy as np
import steering as st

pg.init()

#global variables
#--------------------------------------------

#colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

#sizes
screenSize = (600,600)
carSize = (10,20) #when car is facing upwards

#loading the images
car = pg.image.load("images/car.png")
circuit = pg.image.load("images/circuit")

#scaling the images
circuit = pg.transform.scale(circuit, screenSize)
car = pg.transform.scale(car, carSize)

class car:
    
    def __init__(self, xInit = carSize[0], yInit = carSize[1]):
        
        #initial positions of the car
        self.x = xInit
        self.y = yInit
        
        #initial parameters of the car
        self.abPedal = 0
        self.xSpeed = 0
        self.ySpeed = 0
        self.dirAngle = 90 #car is facing upwards
        self.stAngle = 0

    def updatePos(self, timeInterval = 0.1):
        
        self.dirAngle, self.xSpeed, self.ySpeed = st.getNewSpeed(self.dirAngle, self.xSpeed, self.ySpeed, self.abPedal, self.stAngle, timeInterval)

        self.x += self.xSpeed * timeInterval
        self.y += self.ySpeed * timeInterval 

        





        



