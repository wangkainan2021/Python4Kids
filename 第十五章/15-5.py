import numpy as np
import matplotlib.pyplot as plt

def f(x1, x2):
    return x1**2 + 2 * x1 * x2 + 3

def df_x1(x1, x2):
    return 2 * x1 + 2 * x2

def df_x2(x1, x2):
    return 2 * x1 + 0 * x2

x1 = np.arange(-2, 2 + 0.25, 0.25)
x2 = np.arange(-2, 2 + 0.25, 0.25)

xx1, xx2 = np.meshgrid(x1, x2)

res_f = np.zeros((len(x1), len(x2)))
res_dfx1 = np.zeros((len(x1), len(x2)))
res_dfx2 = np.zeros((len(x1), len(x2)))

for i in range(len(x1)):
    for j in range(len(x2)):
        res_f[i, j] = f(x1[i], x2[j])
        res_dfx1[j, i] = df_x1(x1[i], x2[j])
        res_dfx2[j, i] = df_x2(x1[i], x2[j])

plt.figure(figsize = (10, 5))
plt.subplot(1, 2, 1)
cont = plt.contour(xx1, xx2, res_f, 10)
cont.clabel(fmt = '%d', fontsize = 8)

plt.subplot(1, 2, 2)
plt.quiver(xx1, xx2, res_dfx1, res_dfx2)
plt.show()
