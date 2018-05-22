import os 
import matplotlib.image as img
import numpy as np
import h5py

l_0=[]
m_0=[]

for filename in os.listdir():
	#print (filename)
	l_0.append(filename)

#print(l_0)
l_0.remove('.DS_Store')
l_0.remove('data_es.py')

print (l_0)
for i in l_0:
	im=img.imread(i)
	im.tolist()
	m_0.append(im)

print(len(m_0))
matrix=np.array(m_0)
print(matrix.shape)


f=h5py.File('cat.h5','w')
f['data']=matrix
f.close()


