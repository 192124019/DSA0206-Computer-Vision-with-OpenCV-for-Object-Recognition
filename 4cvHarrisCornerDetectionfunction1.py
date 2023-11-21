import cv2
import numpy as np

# Read the image
image = cv2.imread("C:/Users/USER/Downloads/cvimages.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect corners using Harris Corner Detection
# Parameters: image, block size, ksize, k (Harris detector free parameter)
dst = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)

# Threshold to get only significant corners
threshold = 0.01 * dst.max()
corner_image = np.copy(image)
corner_image[dst > threshold] = [0, 0, 255]  # Mark corners in red

# Display the original and corner-detected images
cv2.imshow('Original Image', image)
cv2.imshow('Corners Detected', corner_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
