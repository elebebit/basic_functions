from PIL import Image  
import os
import cv2
import numpy as np
 
 #Image cpmpression  
def compressImage(srcPath,dstPath):  
    for filename in os.listdir(srcPath):  
        #如果不存在目的目录则创建一个，保持层级结构
        if not os.path.exists(dstPath):
                os.makedirs(dstPath)        
 
        #拼接完整的文件或文件夹路径
        srcFile=os.path.join(srcPath,filename)
        dstFile=os.path.join(dstPath,filename)
        print(srcFile)
        print(dstFile)
 
        #如果是文件就处理
        if os.path.isfile(srcFile):     
            #打开原图片缩小后保存，可以用if srcFile.endswith(".jpg")或者split，splitext等函数等针对特定文件压缩
            sImg=Image.open(srcFile)  
            w,h=sImg.size  
            print (w,h)
            dImg=sImg.resize((800,800),Image.ANTIALIAS)  #设置压缩尺寸和选项，注意尺寸要用括号
            dImg.save(dstFile) #也可以用srcFile原路径保存,或者更改后缀保存，save这个函数后面可以加压缩编码选项JPEG之类的
            print(dstFile+" compressed succeeded")
 
        #如果是文件夹就递归
        if os.path.isdir(srcFile):
            compressImage(srcFile,dstFile)

#diction-merge
def dic_merge():
	global dis_dic

	dis_normal=dict.fromkeys(seq1)
	dis_friend=dict.fromkeys(seq2)

	dis_dic=dict(dis_normal,**dis_friend)

	return dis_dic

def random_choice():
	usr_ls=[]
	rates_ls=[]
	relayd=random.choices(usr_ls,rates_ls,k=1)


def readfolder(dic,pic):
# 不同的mode对应不同的类型
	file_list=os.listdir(dic) 
	t = 0 
	file_temp = ''

	for dic_name in file_list:
		folder=dic+'/'+dic_name
		for root,directors,files in os.walk(folder): 
			for filename in files: 
				filepath = os.path.join(root,filename)
				if (filepath.endswith(".png") or filepath.endswith(".jpg")): 	
					print (filename) 
					#print (remember)
def pic_read(rgb):
	lena = mpimg.imread(rgb) 
	plt.imshow(lena) # 显示图片
	plt.axis('off') # 不显示坐标轴
	plt.savefig()
	plt.show()

#rgb to grey
def rgb2gray(rgb):
	return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

# scatter figure
def scatter_fig(ydata,model):

	yy=np.sum(ydata)
	plt.figure(figsize=(8,6),dpi=100)
	plt.scatter(diss[0:70],ydata[0:70]/yy,marker='x',color='b',label='normal',alpha=0.6)
	plt.scatter(diss[70:100],ydata[70:100]/yy,marker='o',color='r',label='friend',alpha=0.6)
	plt.xticks(fontsize=20)
	plt.yticks(fontsize=20)
	plt.legend(loc='upper right')
	plt.xlabel('location',fontsize=20)
	plt.ylabel('trust degree',fontsize=20)
	plt.savefig('usrstr.eps')

def line_fig(x,y):
	plt.figure(figsize=(8,6),dpi=100)
	#plt.ylim(0,1)
	plt.plot(x,y,"r-",label="$xx$",linewidth=1)
	plt.xlabel('xxx',fontsize=20)
	plt.ylabel('xxx',fontsize=20)
	plt.xticks(fontsize=20)
	plt.yticks(fontsize=20)
	plt.legend()
	plt.savefig('xx.eps')
