x = np.arange(12)
#将x转换为一个3行4列的矩阵
X = x.reshape(3, 4)
#打印矩阵X并换行
print(X)
print("")
#打印矩阵X的全部行和前2列并换行
print(X[:, :2])
print("")
#打印矩阵X的2、3行，以及2，3列
print(X[1:3, 2:4])
