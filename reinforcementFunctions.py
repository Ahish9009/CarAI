import obstacles as ob
import numpy as np
import pygame as pg

def getCrashStatus(carsList, screen, screenSize, carSize, alive):
    
    return list(map(lambda currCar, alive: ob.isOnRoad(screen, screenSize, currCar, carSize) if alive else True, carsList, alive))

def getNextRandom(weights, delta, m, nFeatures):
    
    return ((np.random.rand(m, nFeatures) - 0.5) * delta) + weights

def getRandom(m, nFeatures, delta):
    
    return (np.random.rand(m, nFeatures) - 0.5) * delta

def getAllFeatures(carsList, screen, carSize, screenSize):

    return list(map(lambda x: ob.getFeatures(screen, x, carSize, screenSize, show=0), carsList))

def _assign(car, newAbPedal, newStAngle):
    car.abPedal = newAbPedal
    car.stAngle = newStAngle
    return car

def driveAll(carsList, abPedalWeights, stAngleWeights, screen, carSize, screenSize):

    features = np.array(getAllFeatures(carsList, screen, carSize, screenSize)) #shape is m x nFeatures
    allAbPedals = np.sum(np.multiply(features, abPedalWeights), axis=1) 
    allStAngles = np.sum(np.multiply(features, stAngleWeights), axis=1)

    carsList = list(map(lambda car, newAbPedal, newStAngle: _assign(car, newAbPedal, newStAngle), carsList, allAbPedals, allStAngles))

    return carsList

