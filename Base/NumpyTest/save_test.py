import numpy as np
# save csv 只能是一维二维
np.savetxt("logspace.dat", np.arange(0, 50).reshape(10, 5))
data = np.genfromtxt("logspace.dat")
print(data)

# save npy （推荐）
np.save("logspace.npy", np.arange(100, 150).reshape(5, 10))
d = np.load("logspace.npy")
print(d)

# lst = [[n+m*10 for n in range(5)] for m in range(5)]
lst = np.array([[ 0,  1,  2,  3,  4],
          [10, 11, 12, 13, 14],
          [20, 21, 22, 23, 24],
          [30, 31, 32, 33, 34],
          [40, 41, 42, 43, 44]])
print(lst)
print(lst[:2])
print(type(lst))

e = np.arange(0,25).reshape(5,5)
print(e)
print(e[0:2, 0:2])
print(e[:,0])

#不保存维度信息
f=np.arange(0,20).reshape(4,5)
f.tofile("f.dat",sep=",",format="%d")
g = np.fromfile("f.dat", dtype = np.int, sep=",")
print(g)
