import cv2
import numpy as np

# Load a binary image (you may need to threshold an input image to obtain a binary image)
binary_image = cv2.imread("C:/Users/USER/Downloads/cvimages.jpg", cv2.IMREAD_GRAYSCALE)

# Check if the binary image is loaded successfully
if binary_image is None:
    print("Error: Could not load the binary image.")
    exit()

# Define a kernel for closing
kernel_size = 5
kernel = np.ones((kernel_size, kernel_size), np.uint8)

# Apply closing
closed_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)

# Display the original and closed images
cv2.imshow('Original', binary_image)
cv2.imshow('Closed', closed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
