import numpy as np
import csv

tempTheta = list(csv.reader(open("data/model8.csv")))

theta = np.zeros((len(tempTheta), len(tempTheta[0])))
for i in range(len(tempTheta)):
    for j in range(len(tempTheta[i])):
        theta[i][j] = tempTheta[i][j]

def drive(x):
    
    x = np.array(x)

    toReturn =  x.dot(theta)
    # print(toReturn) 
    
    return toReturn[0], toReturn[1]

    
