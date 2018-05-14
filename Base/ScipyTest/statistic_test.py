import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

X = stats.poisson(3.5) # photon distribution for a coherent state with n=3.5 photons


n = np.arange(0,15)

fig, axes = plt.subplots(3,1, sharex=True)

# plot the probability mass function (PMF)
axes[0].step(n, X.pmf(n))

# plot the commulative distribution function (CDF)
axes[1].step(n, X.cdf(n))

# plot histogram of 1000 random realizations of the stochastic variable X
axes[2].hist(X.rvs(size=1000))

plt.show()