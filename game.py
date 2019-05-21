import pygame as pg
import numpy as np

pg.init()

#global variables
#--------------------------------------------

#colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

#sizes
screenSize = (600,600)
carSize = (20,20)

#loading the images
car = pg.image.load("images/car.png")
circuit = pg.image.load("images/circuit")

#scaling the images
circuit = pg.transform.scale(circuit, screenSize)
car = pg.transform.scale(car, carSize)

