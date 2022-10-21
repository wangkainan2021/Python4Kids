#前两行代码导入数据集和聚类模块。
from sklearn.datasets import load_wine
from sklearn import cluster

#生成数据集和数据对象。
wine = load_wine()
data = wine['data']

#生成k均值模型，指定簇数为3，数据维度选择苹果酸，灰分、灰分
model = cluster.KMeans(n_clusters = 3)
model.fit(data[:, 1:4])

#保存聚类后为数据划分的簇
label = model.labels_

#将苹果酸和灰分碱度作为横纵坐标，输出图像观察聚类情况。
ldata = data[label == 0]
plt.scatter(ldata[:, 1], ldata[:,3], alpha = 0.3, s = 100, marker = "^")
ldata = data[label == 1]
plt.scatter(ldata[:, 1], ldata[:,3], alpha = 0.3, s = 100, marker = "o")
ldata = data[label == 2]
plt.scatter(ldata[:, 1], ldata[:,3], alpha = 0.3, s = 100, marker = "*")
