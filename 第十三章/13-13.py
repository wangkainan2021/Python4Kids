from sklearn import ensemble

model = ensemble.RandomForestRegressor()
model.fit(x, y)

print(model.score(x, y))

plt.scatter(x, y, marker = '+')
plt.scatter(x, model.predict(x), marker = 'o')
plt.show()
