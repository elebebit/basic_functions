import os 
import matplotlib.image as img
import torch
import numpy as np
import h5py
l_0=[]
m_0=[]

for filename in os.listdir():
	print (filename)
	l_0.append(filename)

print(l_0)
l_0.remove('.DS_Store')
l_0.remove('test1.py')

print (l_0)
for i in l_0:
	im=img.imread(i)
	im.tolist()
	m_0.append(im)

print(len(m_0))
nln=np.array(m_0)
print(nln.shape)

f=h5py.File('ph.h5','w')
f['data']=m_0
f['label']=range(100)
f.close()

file=h5py.File('ph.h5','r')
file.keys()
a=file['data'][:]
print(a)
print(a.shape)
