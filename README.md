# Detecting fake faces 

Gabriel Biscaro Cavallari 
#USP 9292862

Facial recognition is being used in many systems and applications. In some cases it's important to detect if fake images are being uploaded by the user to the system in a registration process. This project aims to detect "photoshopped" frontal face images. The goal of this project is to detect likely regions that have been modified using photo editing tools. 

*Main Objective*: Given a frontal face image, detect likely regions that have been modified using photo editing tools. 

*Description of input images*: the dataset contais three groups of fake photos: easy, mid, and hard. It's possible to use the filenames of the fake images to know what have been manipulated:

<img src="filename_description.jpg" width="65%" height="65%"/>

Examples of images:

<img src="samples.jpg" width="65%" height="65%"/>

Source of the images: https://www.kaggle.com/ciplab/real-and-fake-face-detection 

*Steps and methods used*:

1 - Exploring the image color spaces

2 - Denoising methods

3 - Error Level Analysis

4 - Simple filter methods

5 - PCA and LBP (failed attempts)

6 - More examples


The final report is the file **Final_report.ipynb**. The code is the file **Code.ipynb**


