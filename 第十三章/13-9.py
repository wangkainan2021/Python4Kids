print(model.coef_)
print(model.intercept_)
r2 = model.score(x1_x2, y)
print(r2)
