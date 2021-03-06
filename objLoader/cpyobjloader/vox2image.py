import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm
import numpy as np
from scipy.misc import imread
from os.path import dirname
import os
import sys
import time


# alpha channel: non-0 as 1
# rgb channels: assume to between (0,1)
#		otherwise clipped to be (0,1)

def getPoints(vox):
## xs: (n,1)
## rbgs: (n,1)
	vox_a = vox[:,:,:,3]
	xs,ys,zs = np.nonzero(vox_a)
	rgbs = vox[xs,ys,zs,0:3]
	return xs,ys,zs,rgbs

def concatenateImages(imname_list,out_imname):
	N = len(imname_list)
	W = 4
	H = int((N-1)/W)+1
	for i,imname in enumerate(imname_list):
		plt.subplot(H, W, i+1)
		img = imread(imname)
		plt.imshow(img)
	plt.savefig(out_imname,dpi=1000)
	

def vox2image(voxname,imname):
	start = time.time()
	# load .npy file
	vox = np.load(voxname) 	

	# draw 
	fig = plt.figure()
	ax = fig.gca(projection='3d')
	ax.set_aspect("equal")
	dim = vox.shape[0]
	ax.set_xlim(0, dim)
	ax.set_ylim(0, dim)
	ax.set_zlim(0, dim)
	xs,ys,zs,rgbs = getPoints(vox)
	ax.scatter(xs,dim-1-ys, dim-1-zs, color=rgbs, s=5)

	print 'time:', time.time()-start
	plt.savefig(imname)
	

if __name__ == '__main__':
	# test
	#im_list = ["tmp/test1.jpg","tmp/test1.jpg","tmp/test1.jpg","tmp/test1.jpg","tmp/test1.jpg","tmp/test1.jpg","tmp/test1.jpg","tmp/test1.jpg","tmp/test1.jpg"]
	#concatenateImages(im_list, "tmp/test.jpg")	
	#exit(0)

	voxname = os.path.abspath(sys.argv[1])
	imname = os.path.abspath(sys.argv[2])

	# load obj file and convert to vox
	vox2image(voxname,imname)























