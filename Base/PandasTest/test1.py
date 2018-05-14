import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

s = pd.Series([1,3,5,np.nan,6,8])
print(s)

#创建日期索引序列
dates = pd.date_range('20130101', periods=6)
#创建Dataframe，其中 index 决定索引序列，columns 决定列名
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df)


df2 = pd.DataFrame({ 'A' : 1.,
                     'B' : pd.Timestamp('20130102'),
                     'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                     'D' : np.array([3] * 4,dtype='int32'),
                     'E' : pd.Categorical(["test","train","test","train"]),
                     'F' : 'foo' })
print(df2)

print(df.describe())