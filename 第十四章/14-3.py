from sklearn import metrics

target = wine['target']
print(metrics.confusion_matrix(target, label))
