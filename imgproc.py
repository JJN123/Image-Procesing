from scipy import ndimage
from scipy import misc
import numpy as np
from scipy import signal as sg
import matplotlib as ml
import matplotlib.pyplot as plt

#Loading images
imgarr = ndimage.imread("elephant.jpg")

imgarr = imgarr.mean(axis = -1)

a=np.matrix('1. 0 -1.; 2. 0 -2.; 1. 0 -1.')

#Applying various filters 
imgflter = sg.convolve(imgarr,[[1., 1.]],"valid")
misc.imsave('originalgreyscale.png', imgflter)
f_vert = np.matrix('1. 0 -1.; 2. 0 -2; 1. 0 -1.')
imgflter_vert = sg.convolve(imgarr,f_vert,"valid")
misc.imsave('filteredvert.png', imgflter_vert)
f_hor = f_vert.T
imgflter_hor = sg.convolve(imgarr,f_hor,"valid")
misc.imsave('filteredhor.png', imgflter_hor)
 
sigma = 10


def gauss_kern(sigma):
    """ Returns a 2D Gaussian kernel"""
    halfwid = 3*sigma
    x, y = np.mgrid[-halfwid:halfwid+1, -halfwid:halfwid+1]

    gau = np.exp(-1./(2*sigma**2) * (x**2 + y**2))
    return gau/gau.sum()
    #return g / g.sum()
f_blur = gauss_kern(3)

imgflter_blur = sg.convolve(imgarr,f_blur,"valid")
misc.imsave('filteredblur.png', imgflter_blur)

#Fourier xsforms
def fft_helper(arr):
	""" Returns FFT with shift ((0,0) frequency is center)"""

	pre_shift = np.fft.fft2(arr)
	fft = np.fft.fftshift(pre_shift)
	return fft

filter_list = [imgarr, imgflter_vert, imgflter_hor, imgflter_blur, f_vert,f_hor]


orig_fft = fft_helper(imgarr)
vert_fft = fft_helper(imgflter_vert)
hor_fft = fft_helper(imgflter_hor)
blur_fft = fft_helper(imgflter_blur)
f_vert_fft = fft_helper(f_vert)
f_hor_fft = fft_helper(f_hor)
f_blur_fft = fft_helper(f_blur)

fft_dict = {"Original Image FFT": orig_fft , "FFT for Image After Vertical Detection": vert_fft , 
"FFT for Image After Horizontal Detection" : hor_fft, "FFT for Image After Blurring": blur_fft, "FFT for Vertical Filter": f_vert_fft,
 "FFT for Horizontal Filter": f_hor_fft,"FFT for Blurring Filter": f_blur_fft, "Blur Filter in Spatial Domain": f_blur}

def plotter(tile, arr):
	""" Plots image """

	fig, ax = plt.subplots(1, 1)
	ax.imshow(np.log(np.abs(arr)+1), cmap = 'gray')
	#ax.set_title('Plot for {}'.format(title))
	plt.axis('off')
	plt.show()
	misc.imsave('{}.png'.format(title), np.log(np.abs(arr+1)))


for title in fft_dict:
	#Plotting

	arr = fft_dict[title]
	plotter(title, arr)




 