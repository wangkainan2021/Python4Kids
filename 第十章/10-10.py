#将2行3列的<list>转换为矩阵A
A = np.array([[1, 2, 3], [4, 5, 6]])
#输出A的形状
print("矩阵的最初形状为{}".format(A.shape))
#将A的形状改变为3行2列
A = A.reshape(3, 2)
#输出A的形状和A
print("修改后矩阵的形状为{}".format(A.shape))
print(A)
