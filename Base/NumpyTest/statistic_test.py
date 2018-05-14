import numpy as np

a=np.arange(15).reshape(3,5)

np.sum(a)
np.mean(a, axis=1)
np.mean(a, axis=0)
np.average(a, axis=0, weights=[10,5,1])#加权平均
np.std()    #标准差
np.var()    #方差
np.min()    #最小值
np.max()    #最大值
np.argmin() #最小值下标
np.argmax() #最大值下标
np.unravel_index()  #转换为多维下标
np.ptp()            #最大最小值得差
np.median()         #中位数

np.gradient()   #梯度