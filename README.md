# Detecting fake faces 

Gabriel Biscaro Cavallari 
#USP 9292862

Facial recognition is being used in many systems and applications. In some cases it's important to detect if fake images are being uploaded by the user to the system in a registration process. This project aims to detect "photoshopped" frontal face images. The goal of this project is to detect likely regions that have been modified using photo editing tools. 

1. Main Objective: Given a frontal face image, detect likely regions that have been modified using photo editing tools. 

2. The description of input images: the dataset contais three groups of fake photos: easy, mid, and hard. It's possible to use the filenames of fake images to see which part of faces are replaced:

<img src="filename_description.jpg" width="65%" height="65%"/>

Examples of images:

<img src="samples.jpg" width="65%" height="65%"/>

Source of the images: https://www.kaggle.com/ciplab/real-and-fake-face-detection 

3. Steps to reach the objective:

I. Explore simple methods: Simple Thresholding, Adaptive Thresholding, Otsu’s Binarization and multiple filters (high-pass, low-pass etc), texture analysis and color analysis. 

II. Explore some image forensics techniques, such as Noise Detection and Error Level Analysis (ELA). 

III. If those methods aren't enough, train a CNN.  

IV. Since the dataset provides information of which part of faces are replaced, in this step I'll compare my results with the "ground truth", obtaining an accuracy for easy, mid and hard photos. 

Methods that are intented to be used (e.g., image enhancement, edge-detection, morphology, segmentation,texture analysis, color analysis, keypoint detection etc.):

It should also present some initial code with the first results obtained analysing the images.

