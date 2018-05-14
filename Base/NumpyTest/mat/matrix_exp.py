# -*- coding: utf-8 -*-

# 导入 numpy 函数，以 np 开头
import numpy as np

if __name__ == '__main__':
    mat1 = np.array([1, 3])
    mat1 = np.mat(mat1)  # 相当于 np.mat([1,3])， mat 函数将目标数据的类型转换为矩阵（matrix）
    print( mat1 )
    # 1 行 2 列的矩阵（也称 1 * 2 矩阵）
    # ==> [[1 3]]

    mat2 = np.array([[1, 3], [3, 4]])
    mat2 = np.mat(mat2)
    print( mat2 )
    # 2 * 2 矩阵
    # ==> [[1 3]
    # ==>  [3 4]]

    # 获取矩阵的大小
    print( mat1.shape )
    print( mat2.shape )

    mat3 = np.zeros((2, 3))  # 2 * 3 的全 0 矩阵
    mat4 = np.ones((3, 2))   # 3 * 2 的全 1 矩阵
    mat5 = np.identity(3)    # 3 * 3 的单元矩阵
    mat6 = np.eye(3, 3, 0)   # eye(N, M=None, k=0, dtype=float) 对角线是 1 其余值为 0 的矩阵, k 指定对角线的位置
    print( mat3 )
    print( mat4 )
    print( mat5 )
    print( mat6 )