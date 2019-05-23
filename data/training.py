import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math, csv

nFeatures = 6
nOutput = 2

def costFunction(x, y, theta):
    
    m = len(y)
    cost = [0 for j in range(nOutput)]

    estimated = x.dot(theta)
    for i in range(m):

        for j in range(nOutput):
            cost[j] += (y[i][j] - estimated[i][j])**2

    for i in range(nOutput):
        cost[i]/=m
    
    # print(cost)

    return cost

def gradDescent(x, y, theta, alpha):

    m = len(y)
    estimated = x.dot(theta)
    
    # print(len(theta))

    for i in range(len(theta)):

        derivative = [0 for j in range(nOutput)]
        for j in range(m):

            for k in range(nOutput):
                derivative[k] += (estimated[j][k] - y[j][k])*x[j][i]
        
        # print(derivative)

        for j in range(nOutput):
            theta[i][j] -= (alpha*derivative[j])/m
    return theta

allData = list(csv.reader(open("features.csv")))

X = np.zeros((len(allData), nFeatures))
Y = np.zeros((len(allData), nOutput))
theta = np.random.uniform(low = -2, high = 2, size = (nFeatures, nOutput))

for i in range(len(allData)):
    for j in range(nFeatures):
        X[i][j] = allData[i][j]
    for j in range(nFeatures, nFeatures + nOutput):
        Y[i][j - nFeatures] = allData[i][j]

nIterations = 230
alpha = (0.0001+0.00001)/2

toPlotY1 = []
toPlotY2 = []

estimated = X.dot(theta)
# print(estimated)

i = 0
while i < nIterations:
    
    theta = gradDescent(X, Y, theta, alpha)
    cost = costFunction(X, Y, theta)
    
    # print(X.dot(theta))

    toPlotY1 += [cost[0]]
    toPlotY2 += [cost[1]]
    
    if i == nIterations-1:
        print(cost)
        cont = input()
        print(cont)
        if cont == '':
            nIterations += 10
    
    i+=1

np.savetxt("model8.csv", theta, delimiter = ',')


print(cost)
print(theta)

toPlotX = range(1,nIterations+1)
plt.plot(toPlotX, toPlotY1, color='blue')
plt.plot(toPlotX, toPlotY2, color='red')
plt.show()










