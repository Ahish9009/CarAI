import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math, csv

nFeatures = 11
nTotalFeatures = 31
nOutput = 2

def getPowerCol(x, colInit, colDest, power):
    
    m = len(x)

    for i in range(m):

        x[i][colDest] = x[i][colInit]**power

    return x


def costFunction(x, y, theta):
    
    m = len(y)
    cost = [0 for j in range(nOutput)]

    estimated = x.dot(theta)
    
    # print(estimated)
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

X = np.zeros((len(allData), nTotalFeatures))
Y = np.zeros((len(allData), nOutput))
theta = np.random.uniform(low = -0.05, high = 0.05, size = (nTotalFeatures, nOutput))

for i in range(len(allData)):
    for j in range(nFeatures):
        X[i][j] = allData[i][j]
    for j in range(nFeatures, nFeatures + nOutput):
        Y[i][j - nFeatures] = allData[i][j]

for i in range(nFeatures-1):

    X = getPowerCol(X, i, nFeatures+i, 2)
    X = getPowerCol(X, i, nFeatures+10+i, 3)

print(X[0])
input()


nIterations = 100
# alpha = (  0.00001 + 0.0001 ) /2
alpha= 0.00000000000001

toPlotY1 = []
toPlotY2 = []

estimated = X.dot(theta)
# print(estimated)

# i = 0
# while i < nIterations:

    # if (i%10 == 0):
        # print(i)

    # theta = gradDescent(X, Y, theta, alpha)
    # cost = costFunction(X, Y, theta)
    
    # # print(X.dot(theta))

    # toPlotY1 += [cost[0]]
    # toPlotY2 += [cost[1]]
    # # print(cost)

    # if i == nIterations-1:
        # print(cost)
        # print(theta)
        # cont = input()
        # print(cont)
        # if cont == '':
            # nIterations += 100
    
    # i+=1

# np.savetxt("model5.csv", theta, delimiter = ',')

# normal method
new = np.linalg.inv((np.matrix.transpose(X)).dot(X)).dot(np.matrix.transpose(X).dot(Y))
print(new)
print(costFunction(X, Y, new))
np.savetxt("normalModel8.csv", new, delimiter = ',')

# print(cost)
# print(theta)

# toPlotX = range(1,nIterations+1)
# plt.plot(toPlotX, toPlotY1, color='blue')
# plt.plot(toPlotX, toPlotY2, color='red')
# plt.show()










