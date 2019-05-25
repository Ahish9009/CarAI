import numpy as np
import csv

nFeatures = 11

tempTheta = list(csv.reader(open("data31Features/normalModel3.csv")))

theta = np.zeros((len(tempTheta), len(tempTheta[0])))
for i in range(len(tempTheta)):
    for j in range(len(tempTheta[i])):
        theta[i][j] = tempTheta[i][j]


def getPowerCol(x, colInit, colDest, power):
    
    x[colDest] = x[colInit]**power

    return x

def normalize(x):

    for j in range(9):
        x[j]/=300.
    x[9]/=30.

    # print(x)
    return x

def drive(inp):

    x = np.zeros(31)
   
    for i in range(11):
        x[i] = inp[i]
    # x = normalize(x)
    

    for i in range(nFeatures-1):

        x = getPowerCol(x, i, nFeatures+i, 2)
        x = getPowerCol(x, i, nFeatures+10+i, 3)

    toReturn =  x.dot(theta)
    # print(toReturn) 
    
    return toReturn[0], toReturn[1]

    
