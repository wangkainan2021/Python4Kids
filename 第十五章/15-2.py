import os
import glob
import numpy as np
from skimage import io
from sklearn.utils import Bunch

W = 75
H = 100
COLOR_BYTE = 3
CATEGORY_NUM = 3

def load_handimage(path):
    files = glob.glob(os.path.join(path, '*/*.jpg'))
    images = np.ndarray((len(files), H, W, COLOR_BYTE), dtype = np.uint8)
    labels = np.ndarray(len(files), dtype = int)
    
    for idx, file in enumerate(files):
        image = io.imread(file)
        images[idx] = image
        label = os.path.split(os.path.dirname(file))[-1]
        labels[idx] = label
        
    
    flat_data = images.reshape((-1, H * W * COLOR_BYTE))
    images= flat_data.view()
    return Bunch(data = flat_data,
                     target = labels.astype(int),
                     target_names = np.arange(CATEGORY_NUM),
                     image =images,
                     DESCR = None)
