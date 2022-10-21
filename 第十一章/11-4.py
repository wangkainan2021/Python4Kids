import numpy as np
import matplotlib.pyplot as plt

#绘制笛卡尔心型线所需的t, x, y
t = np.linspace(0, 10, 100)
x = 2 * np.cos(t) - np.cos(2 * t)
y = 2 * np.sin(t) - np.sin(2 * t)

plt.figure()
#设置图形为粉色，图例名称为heart line
plt.plot(y, x, color='pink', label = 'heart line')
#将图例显示在右上角
plt.legend(loc = "upper right") 
#定义x, y轴范围
plt.xlim(-4, 4)
plt.ylim(-4, 2)
#图形的标题
plt.title("Cartesian heart-shaped line")
#添加x、y轴标签
plt.xlabel('$x$')
plt.ylabel('$y$')
#显示网格线
plt.grid(True)

plt.show()
