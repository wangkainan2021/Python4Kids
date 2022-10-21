from sklearn.datasets import load_wine
from sklearn import cluster
from sklearn.model_selection import train_test_split

wine = load_wine()
data = wine['data']
target = wine['target']

#model = cluster.KMeans(n_clusters = 3)
model = cluster.AffinityPropagation()
model.fit(data[:, 1:4])

label = model.labels_
marker = [".", ",", "o", "v", "^", "<", ">", "1", "2", "3", "4", "8","s","p"]
for i in range(max(label)):
    ldata = data[label == i]
    plt.scatter(ldata[:, 1], ldata[:,3], alpha = 0.3, s = 100, marker = marker[i])
