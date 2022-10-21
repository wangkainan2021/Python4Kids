import numpy as np
import matplotlib.pyplot as plt

x = np.arange(10)
y1 = 4 * x + 15
y2 = x**2

plt.figure()
plt.plot(x, y1)
plt.plot(x, y2, color = "red")
plt.show()
