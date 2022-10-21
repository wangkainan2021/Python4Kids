from sklearn import metrics

print("准确率:", metrics.accuracy_score(y_test, y_pred))
print("混淆矩阵:\n", metrics.confusion_matrix(y_test, y_pred))
print("查准率:", metrics.precision_score(y_test, y_pred, average=None))
print("查全率:", metrics.recall_score(y_test, y_pred, average=None))
print("F值:", metrics.f1_score(y_test, y_pred, average=None))
