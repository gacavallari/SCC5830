# Detecting fake faces 

Gabriel Biscaro Cavallari 
#USP 9292862

Facial recognition is being used in many systems and applications. In some cases it's important to detect if fake images are being uploaded by the user to the system in a registration process. This project aims to detect "photoshopped" frontal face images. Exploring image description and deep learning techniques, the goal of this project is to detect likely regions that have been modified using photo editing tools. 

1. Main Objective: Given a frontal face image, detect likely regions that have been modified using photo editing tools. 

2. The description of input images (with examples) including the source of the images
<img src="samples.jpg" width="65%" height="65%"/>

Source of the images: https://www.kaggle.com/ciplab/real-and-fake-face-detection 

3. Steps to reach the objective:

I. Explore simple methods: Simple Thresholding, Adaptive Thresholding and Otsu’s Binarization
II. Explore some image forensics techniques, such as noise reduction filter (separable Median Filter) (Noise detection?) and Error Level Analysis (ELA). 
III. Compare the results with the "ground truth".

Methods that are intented to be used (e.g., image enhancement, edge-detection, morphology, segmentation,texture analysis, color analysis, keypoint detection etc.):

It should also present some initial code with the first results obtained analysing the images.

