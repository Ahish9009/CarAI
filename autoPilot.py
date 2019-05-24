import numpy as np
import csv

nFeatures = 11

tempTheta = list(csv.reader(open("data11Features/hybrid2.csv")))

theta = np.zeros((len(tempTheta), len(tempTheta[0])))
for i in range(len(tempTheta)):
    for j in range(len(tempTheta[i])):
        theta[i][j] = tempTheta[i][j]


def normalize(x):

    for j in range(6):
        x[j]/=600
    return x

def drive(x):
    
    x = np.array(x)
    # x = normalize(x)

    toReturn =  x.dot(theta)
    # print(toReturn) 
    
    return toReturn[0], toReturn[1]

    
