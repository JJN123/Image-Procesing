# Image-Proccesing
Playing around with some image proccessing techniques (2-d FFT/ convolution).
See wiki for details on use of code.

Welcome to the Image-Processing wiki!

In this project, I apply various filters to the following image:

![](https://github.com/JJN123/Image-Procesing/blob/master/originalgreyscale.png)

For example, after applying a Gaussian filter:

![](https://github.com/JJN123/Image-Procesing/blob/master/filteredblur.png)

To understand the results of each filter, I examined their fft's. For example, we can see why the above image is blurred after a Gaussian filter is applied. The fft of a Gaussian filter is another Gaussian, which has darker regions moving radially outward (direction of increasing frequency).

By the convolution theorem, the dark regions of the Gaussian filter fft will multiply the high frequency regions of the filtered signals frequency spectrum. This explains the above result; edges (high frequency) are blurred.

Gaussian Filter:
![](https://github.com/JJN123/Image-Procesing/blob/master/blurspatialnoax.png)

FFT of Gaussian Filter:

![](https://github.com/JJN123/Image-Procesing/blob/master/Blurfilterfftnoax.png)

Applying the Sobel filter results in edge detection, for example the y-Sobel filter gives:

![](https://github.com/JJN123/Image-Procesing/blob/master/filteredvert.png)
