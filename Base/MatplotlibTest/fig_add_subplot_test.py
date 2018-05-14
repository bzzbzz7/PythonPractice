import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 50)
y1 = 2 * x + 1
y2 = x ** 2 + 1

fig = plt.figure(figsize=(8,4), dpi=80)
fig.set_facecolor("gray")

p1 = fig.add_subplot(2,1,1)
p1.plot(x, y1, "r-", label="2*x + 1")
p1.set_title("y1")
p1.legend()

p2 = fig.add_subplot(2,1,2)
p2.plot(x, y2, "b*", label=r"$y=x^2+1$")
p2.set_title("y2")
p2.legend()

plt.show()
