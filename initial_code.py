import imageio
import cv2
import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as la
import matplotlib as mp
from skimage.exposure import rescale_intensity


def filtering_3d(img, filter_w):
    
    # initialize the processed image with the same shape of the input image
    filtered_img = np.zeros((img.shape[0], img.shape[1]))
    
    n = filter_w.shape[0]
    # considering that the array starts at position 0, gives the "center" position of the filter
    center = int(np.floor(n/2))
    
    # symmetric pad the input image
    #img[:,:,0] = np.pad(img[:,:,0], center, mode='symmetric')
    #print(img.shape)
    
    # calculate all the pixels of the processed image
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            try:
                filtered_img[i,j] = (np.sum(img[i:i+n, j:j+n,0]*filter_w) + 
                                    np.sum(img[i:i+n, j:j+n,1]*filter_w) +
                                    np.sum(img[i:i+n, j:j+n,2]*filter_w))

            except: 
                pass

    return filtered_img


    

img = imageio.imread('./data/fake_images/easy_57_0010.jpg')
print(img.shape[2])

laplacian = np.array((
	[0, 1, 0],
	[1, -4, 1],
	[0, 1, 0]), dtype="int")



#filter_w = np.asarray(filter_w)
#filtered_img = filtering_3d(img, laplacian)
#output = rescale_intensity(filtered_img, in_range=(0, 255))
#output = (output * 255).astype("uint8")
#plt.imshow(output)
#plt.show()

def simple_thresholding(img_path):

    img = cv2.imread(img_path,0)
    ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
    ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
    ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
    ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

    titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
    images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

    for i in range(6):
        plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])

    plt.show()

def adaptative_thresholding(img_path):
    img = cv2.imread(img_path,0)
    img = cv2.medianBlur(img,5)

    ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                cv2.THRESH_BINARY,11,2)
    th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                cv2.THRESH_BINARY,11,2)

    titles = ['Original Image', 'Global Thresholding (v = 127)',
                'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
    images = [img, th1, th2, th3]

    for i in range(4):
        plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])
    plt.show()

def otsu(img_path):
    img = cv2.imread(img_path,0)

    # global thresholding
    ret1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

    # Otsu's thresholding
    ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    # Otsu's thresholding after Gaussian filtering
    blur = cv2.GaussianBlur(img,(5,5),0)
    ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    # plot all the images and their histograms
    images = [img, 0, th1,
            img, 0, th2,
            blur, 0, th3]
    titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
            'Original Noisy Image','Histogram',"Otsu's Thresholding",
            'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]

    for i in range(3):
        plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
        plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
        plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
        plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
        plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
        plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
    plt.show()

def image_blurring(img_path):
    img = cv2.imread(img_path,0)

    blur = cv2.blur(img,(5,5))

    plt.subplot(121),plt.imshow(img),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(blur),plt.title('AveragingBlur')
    plt.xticks([]), plt.yticks([])
    plt.show()

    blur = cv2.GaussianBlur(img,(5,5),0)
    plt.subplot(121),plt.imshow(img),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(blur),plt.title('GaussianBlur')
    plt.xticks([]), plt.yticks([])
    plt.show()

    blur = cv2.medianBlur(img,5)
    plt.subplot(121),plt.imshow(img),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(blur),plt.title('MedianBlur')
    plt.xticks([]), plt.yticks([])
    plt.show()

    blur = cv2.bilateralFilter(img,9,75,75)
    plt.subplot(121),plt.imshow(img),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(blur),plt.title('bilateralFilter')
    plt.xticks([]), plt.yticks([])
    plt.show()

def high_pass_filters(img_path):
    img = cv2.imread(img_path,0)

    laplacian = cv2.Laplacian(img,cv2.CV_64F)
    sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
    sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
    
    plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
    plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
    plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
    plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

    plt.show()

def canny_edge(img_path):

    img = cv2.imread(img_path,0)
    edges = cv2.Canny(img,100,200)

    plt.subplot(121),plt.imshow(img,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

    plt.show()


simple_thresholding('./data/fake_images/easy_57_0010.jpg')
adaptative_thresholding('./data/fake_images/easy_57_0010.jpg')
otsu('./data/fake_images/easy_57_0010.jpg')
#image_blurring('./data/fake_images/easy_57_0010.jpg')
#high_pass_filters('./data/fake_images/easy_57_0010.jpg')
#canny_edge('./data/fake_images/easy_57_0010.jpg')

import skimage.segmentation as seg
from scipy.signal import medfilt 

#image_slic = seg.slic(img,n_segments=500)
#plt.imshow(image_slic)

#image_felzenszwalb = seg.felzenszwalb(img)
#plt.imshow(image_felzenszwalb)

#img = cv2.imread('./data/fake_images/easy_57_0010.jpg', 0)
#img_median = medfilt(img, 17)
#plt.imshow(255-img_median, cmap='gray')


#plt.show()