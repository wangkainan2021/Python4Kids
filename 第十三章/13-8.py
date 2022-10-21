model.fit(x1_x2, y)
y_ = model.predict(x1_x2)

plt.subplot(1, 2, 1)
plt.scatter(x1, y, marker = '+')
plt.scatter(x1, y_, marker = 'o')

plt.subplot(1, 2, 2)
plt.scatter(x2, y, marker = '+')
plt.scatter(x2, y_, marker = 'o')

plt.tight_layout()
plt.show()
