from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1 / 3, random_state = 0)
clr = SVC(C = 0.5, kernel = "linear", decision_function_shape='ovr', probability = True)
clr.fit(X_train, y_train)
y_pred = clr.predict(X_test)
score = clr.score(X_test, y_test)
print("准确率：", score)
print(y_pred)
print(y_test)
