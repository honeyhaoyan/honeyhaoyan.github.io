import numpy as np

# 定义矩阵
A = np.array([[4,6,0],
              [-3,-5,0],
              [-3,-6,1]])

# 计算逆矩阵
A_inv = np.linalg.inv(A)

print(A_inv)