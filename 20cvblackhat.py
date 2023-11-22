import cv2
import numpy as np

# Load a grayscale image
image = cv2.imread("C:/Users/USER/Downloads/cvimages.jpg", cv2.IMREAD_GRAYSCALE)

# Check if the image is loaded successfully
if image is None:
    print("Error: Could no5t load the image.")
    exit()

# Define a kernel for the black hat operation
kernel_size = 15
kernel = np.ones((kernel_size, kernel_size), np.uint8)

# Apply black hat operation
blackhat = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)

# Display the original and black hat images
cv2.imshow('Original', image)
cv2.imshow('Black Hat', blackhat)
cv2.waitKey(0)
cv2.destroy
