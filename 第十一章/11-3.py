import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-3, 3, 0.1)
y = np.array([np.sin(i) for i in x])
plt.scatter(x, y, color = 'green', alpha = 0.2, marker = '*')
plt.show()
