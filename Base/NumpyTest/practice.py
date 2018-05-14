import numpy as np

a = np.arange(1, 100, dtype=np.float)
print(a)

b = np.linspace(0, 100, endpoint=False)
print(b)

print(101 / 50)

c = np.logspace(0, 10)
print(c)

x, y = np.mgrid[0:5, 0:5]
print(x)
print(y)



