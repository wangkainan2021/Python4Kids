import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

x1 = np.array([1.78, 1.7, 1.9, 1.83, 1.73, 2.06, 1.8, 1.77, 1.88, 1.7])
x2 = np.array([1.56, 1.55, 1.8, 1.63, 1.62, 1.8, 1.75, 1.67, 1.8, 1.55])
x1_x2 = np.c_(x1, x2)
