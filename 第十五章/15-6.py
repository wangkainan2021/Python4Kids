import os
import sys
import glob
import numpy as np
from skimage import io
from sklearn.utils import Bunch
from skimage.feature import hog

from sklearn.model_selection import GridSearchCV

param_grid = {
    'C':[1, 10, 100],
    'loss':['hinge', 'squared_hinge']
}

W = 75
H = 100
COLOR_BYTE = 3
CATEGORY_NUM = 3

def load_handimage(path):
    files = glob.glob(os.path.join(path, '*/*.jpg'))
    
    hogs = np.ndarray((len(files), 39600), dtype = float)
    
    images = np.ndarray((len(files), H, W, COLOR_BYTE), dtype = np.uint8)
    labels = np.ndarray(len(files), dtype = int)
    
    for idx, file in enumerate(files):
        image = io.imread(file, as_gray=True)
        h = hog(image, orientations=9, pixels_per_cell=(5,5), cells_per_block=(5,5))
        hogs[idx] = h
        
        label = os.path.split(os.path.dirname(file))[-1]
        labels[idx] = label
        
    return Bunch(data = hogs,
                     target = labels.astype(int),
                     target_names = np.arange(3),
                     DESCR = None)

from sklearn import svm, tree, ensemble,  metrics

train = load_handimage('C:\\Users\\wkn_4\\Pictures\\Rock-Paper-Scissors\\tot_train')
test = load_handimage('C:\\Users\\wkn_4\\Pictures\\Rock-Paper-Scissors\\tot_test')

clf = GridSearchCV(svm.LinearSVC(), param_grid)
clf.fit(train.data, train.target)
predicted = clf.predict(test.data)
print("准确率:{}".format(metrics.accuracy_score(test.target, predicted)))

print("最佳参数组合:{}".format(clf.best_estimator_))

