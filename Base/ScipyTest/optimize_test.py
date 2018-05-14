import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt


def f(x):
    return 4 * x ** 3 + (x - 2) ** 2 + x ** 4

x = np.linspace(-5, 3, 100)
plt.plot(x, f(x));
plt.show()

x_min = optimize.fmin_bfgs(f, -2)
print(x_min)
