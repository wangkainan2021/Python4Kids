import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

fig = plt.figure(figsize = (10, 5))

#生成一个3D图对象ax
ax = fig.add_subplot(projection = '3d')

#绘制3D图形
#生成向量x, y
x = np.arange(-5, 5, 0.25)
y = np.arange(-5, 5, 0.25)
#对应到3d图形所需坐标向量
x, y = np.meshgrid(x, y)
#根据x,y的值生成z
z = np.sin(np.sqrt(x**2 + y**2))

#设置3D图形的x,y,z数据，颜色方案
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm, antialiased=False)
#设置z轴范围[-1.01, 1.01]
ax.set_zlim(-1.01, 1.01)
#设置显示色阶的颜色栏
fig.colorbar(mappable = surf, shrink=0.5, aspect=10)
