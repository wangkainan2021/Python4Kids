import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA

# 将实际分类结果存在数组y中，作为圆点颜色使用
iris = datasets.load_iris()
y = iris.target

# 准备画图
fig = plt.figure(1, figsize=(8, 6))
ax = Axes3D(fig, elev=-150, azim=110)
X_reduced = PCA(n_components=3).fit_transform(iris.data)
ax.scatter(
    X_reduced[:, 0],
    X_reduced[:, 1],
    X_reduced[:, 2],
    c=y,  
    cmap=plt.cm.Set1,
    edgecolor="k",
    s=40,
)
ax.set_xlabel("len_sepal")  #萼片的长度
ax.w_xaxis.set_ticklabels([])
ax.set_ylabel("width_sepal")  #萼片的宽度
ax.w_yaxis.set_ticklabels([])
ax.set_zlabel("len_petal")  #花瓣的长度
ax.w_zaxis.set_ticklabels([])

plt.show()
