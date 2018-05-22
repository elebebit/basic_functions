import numpy as np

from sklearn.decomposition import PCA
import h5py
import torch
import torch.nn as nn


dog=h5py.File('dog.h5','r')
dog.keys()
d=dog['data'][:]

print(d.shape)

dx=d.reshape((349,1920000))
ddx=torch.IntTensor(dx)
b=ddx.tolist()

#where_are_nan=np.isnan(dx)
#dx[where_are_nan]=0



pca=PCA(n_components=8)

#print(x.shape)
print(pca)
y=pca.fit_transform(b)

print(pca.explained_variance_ratio_)
print(y)

