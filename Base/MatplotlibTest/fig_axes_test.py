import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 50)
y1 = 2 * x + 1
y2 = x ** 2 + 1

fig = plt.figure()
axes1 = fig.add_axes([0.1, 0.1, 0.9, 0.9])
axes1.plot(x, y1, "r-", label="y1 = 2 * x + 1")
axes1.set_title("y1")

axes2 = fig.add_axes([0.2, 0.2, 0.3, 0.3])
axes2.plot(x, y2, "b*", label=" x ** 2 + 1")
axes2.set_title("y2")

plt.show()
