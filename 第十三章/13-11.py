from sklearn import linear_model
model = linear_model.LinearRegression()
model.fit(x, y)

print(model.score(x, y))

plt.scatter(x, y, marker = '+')
plt.scatter(x, model.predict(x), marker = 'o')
plt.show()
