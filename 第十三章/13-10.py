import math
import numpy as np
import matplotlib.pyplot as plt

#生成1000个[0, 1]之间的随机数
x = np.random.rand(1000, 1)
#将值的范围变更[-10, 10]
x = x * 20 - 10

#创建对应的 向量y
y = np.array([math.cos(i) for i in x])
#附加噪声
y += np.random.randn(1000)
