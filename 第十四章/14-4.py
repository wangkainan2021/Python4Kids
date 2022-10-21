from sklearn.datasets import load_wine
from sklearn import cluster
from sklearn.model_selection import train_test_split

wine = load_wine()
data = wine['data']
target = wine['target']

#model = cluster.KMeans(n_clusters = 3)
model = cluster.AgglomerativeClustering(n_clusters = 3, linkage ='ward')
model.fit(data[:, 1:4])

label = model.labels_

ldata = data[label == 0]
plt.scatter(ldata[:, 1], ldata[:,3], alpha = 0.3, s = 100, marker = "^")
ldata = data[label == 1]
plt.scatter(ldata[:, 1], ldata[:,3], alpha = 0.3, s = 100, marker = "o")
ldata = data[label == 2]
plt.scatter(ldata[:, 1], ldata[:,3], alpha = 0.3, s = 100, marker = "*")
