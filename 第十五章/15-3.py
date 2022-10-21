from sklearn import svm, metrics

train = load_handimage('C:\\Users\\wkn_4\\Pictures\\Rock-Paper-Scissors\\train')
test = load_handimage('C:\\Users\\wkn_4\\Pictures\\Rock-Paper-Scissors\\test')

clf = svm.LinearSVC()
clf.fit(train.data, train.target)
predicted = clf.predict(test.data)
print("准确率:{}".format(metrics.accuracy_score(test.target, predicted)))
