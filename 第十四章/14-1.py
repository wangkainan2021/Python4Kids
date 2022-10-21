#首先导入数据集模块
from sklearn import datasets 

#生成红酒数据集对象
wine = datasets.load_wine()
#输出数据集的维度形状
print(wine['data'].shape)
#输出数据的特征
print(wine.feature_names)
