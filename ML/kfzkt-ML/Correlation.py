import numpy as np
# from astropy.units import Ybarn
import math


def computeCorrelation(X, Y):
    xBar = np.mean(X)
    yBar = np.mean(Y)
    SSR = 0
    varX = 0
    varY = 0
    for i in range(0, len(X)):
        diffXXBar = X[i] - xBar
        diffYYBar = Y[i] - yBar
        SSR += (diffXXBar * diffYYBar)
        varX += diffXXBar ** 2
        varY += diffYYBar ** 2

    SST = math.sqrt(varX * varY)
    return SSR / SST


testX = [1, 3, 8, 7, 9]
testY = [10, 12, 24, 21, 34]

print(computeCorrelation(testX, testY))
