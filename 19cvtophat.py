import cv2
import numpy as np

# Load a grayscale image
image = cv2.imread("C:/Users/USER/Downloads/cvimages.jpg", cv2.IMREAD_GRAYSCALE)

# Check if the image is loaded successfully
if image is None:
    print("Error: Could not load the image.")
    exit()

# Define a kernel for the top hat operation
kernel_size = 15
kernel = np.ones((kernel_size, kernel_size), np.uint8)

# Apply top hat operation
tophat = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)

# Display the original and top hat images
cv2.imshow('Original', image)
cv2.imshow('Top Hat', tophat)
cv2.waitKey(0)
cv2.destroyAllWindows()
