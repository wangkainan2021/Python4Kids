plt.scatter(x, y, marker ='+')
plt.plot(x, model.predict(x), c = 'r')
plt.show()
