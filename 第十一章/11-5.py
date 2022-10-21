import numpy as np
import matplotlib.pyplot as plt

#定义一个三次函数 y = (x - w)·x·(x - 3) 
def f(x, w):
    return (x - w) * x * (x - 3)

#生成[-5, 5)以0.01为跨度的向量x
x = np.arange(-5, 5, 0.01)
#设置画布宽度为 10 * 5,单位为英寸
plt.figure(figsize= (10, 5))
#设置子图之间的宽高填充，防止子图的信息挤到一起
plt.subplots_adjust(wspace = 0.5, hspace = 0.5)

for i in range(1, 7):
    #以2行3列的方式展示子图
    plt.subplot(2, 3, i)
    #每个子图的标题为编号 i
    plt.title(i)
    #绘制三次函数图形
    plt.plot(x, f(x, i))
    #设置y轴范围为[-100, 100]
    plt.ylim(-100, 100)
    #显示网格线
    plt.grid(True)
