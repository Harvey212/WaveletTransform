import cv2
from scipy.signal import convolve2d
import numpy as np
from scipy import signal
from skimage.measure import block_reduce

def conv2d(im,fil):
	return np.rot90(convolve2d(np.rot90(im,2),np.rot90(fil,2),mode='same', boundary='symm'),2)

def wavedbc6(g,h,arr):
	gT=g.transpose()
	hT=h.transpose()
	#################################
	xg=conv2d(arr,g)
	xgT=xg.transpose()
	v1L=(block_reduce(xgT,func=np.mean)).transpose()
	########################################
	xh=conv2d(arr,h)
	xhT=xh.transpose()
	v1H=(block_reduce(xhT,func=np.mean)).transpose()
	##########################################################
	v1Lg=conv2d(v1L,gT)
	x1L=(block_reduce(v1Lg,func=np.mean))
	##############################
	v1Lh=conv2d(v1L,hT)
	x1H1=block_reduce(v1Lh,func=np.mean)
	############################
	v1Hg=conv2d(v1H,gT)
	x1H2=block_reduce(v1Hg,func=np.mean)
	###########################
	v1Hh=conv2d(v1H,hT)
	x1H3=block_reduce(v1Hh,func=np.mean)

	return x1L, x1H1, x1H2, x1H3

def myshow(temp,scale):
	new_image=np.zeros((temp.shape[0],temp.shape[1]),dtype=np.uint8)
	for i in range(temp.shape[0]):
		for j in range(temp.shape[1]):
			if temp[i][j]>0:
				new_image[i][j]=temp[i][j]*scale

	cv2.imshow('img',new_image)
	cv2.waitKey(0)
				
def iwavedbc6(g1,h1,x1L, x1H1, x1H2, x1H3):
	g1T=g1.transpose()
	h1T=h1.transpose()

	X1L=np.repeat(x1L,2, axis=1).repeat(2, axis=0)
	X1H1=np.repeat(x1H1,2, axis=1).repeat(2, axis=0)
	x0=conv2d(X1L,g1T)+conv2d(X1H1,h1T)
	x0T=x0.transpose()
	#################################3
	X1H2=np.repeat(x1H2,2, axis=1).repeat(2, axis=0)
	X1H3=np.repeat(x1H3,2, axis=1).repeat(2, axis=0)
	x1=conv2d(X1H2,g1T)+conv2d(X1H3,h1T)
	x1T=x1.transpose()
	################################
	X0=(np.repeat(x0T,2, axis=1).repeat(2, axis=0)).transpose()
	X1=(np.repeat(x1T,2, axis=1).repeat(2, axis=0)).transpose()

	com=conv2d(X0,g1)+conv2d(X1,h1)

	return com
	#############################
##############################################
gg=np.array([[0.0352,-0.0854,-0.1350,0.4599,0.8069,0.3327]])#
hh=np.array([[0.3327,-0.8069,0.4599,0.1350,-0.0854,-0.0352]])#

gg1=np.array([[0.3327,0.8069,0.4599,-0.1350,-0.0854,0.0352]])
hh1=np.array([[-0.0352,-0.0854,0.1350,0.4599,-0.8069,0.3327]])
##################################
image = cv2.imread('pic.png')
arr1=image[:,:,0]

x1L, x1H1, x1H2, x1H3=wavedbc6(gg,hh,arr1)

########################
myshow(x1L,255/500)
myshow(x1H1,10)
myshow(x1H2,40)
myshow(x1H3,150)
##########################################
final=iwavedbc6(gg1,hh1,x1L, x1H1, x1H2, x1H3)
myshow(final,255/1000)




