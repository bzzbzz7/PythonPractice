import numpy as np
from scipy import linalg

A = np.array([[1, 2, 3], [4, 2, 6], [7, 8, 5]])
b = np.array([1, 2, 3])

c = linalg.solve(A, b)
print(c)

A=np.random.rand(3,3)
B=np.random.rand(3,3)
c=linalg.solve(A,B)
print(c)

A=np.random.randint(0,25,[5,5])
evals = linalg.eigvals(A)
print(evals)