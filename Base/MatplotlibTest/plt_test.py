import numpy as np
import matplotlib.pyplot as plt


x=np.linspace(-1,1,50)
y1=2*x+1
plt.figure()
plt.plot(x,y1)
plt.title("f1")

y2=x**2 + 1
plt.figure()
plt.plot(x,y2)
plt.title("f2")
plt.show()


