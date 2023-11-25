import cv2
import numpy as np

# Read the image
image = cv2.imread('cv.png', 0)  # Read the image in grayscale

# Apply Gaussian blur to reduce noise
image_blurred = cv2.GaussianBlur(image, (3, 3), 0)

# Calculate the Laplacian
laplacian = cv2.Laplacian(image_blurred, cv2.CV_64F)

# Convert the result to a uint8 type array to avoid missing any edges
laplacian_abs = np.uint8(np.absolute(laplacian))

# Display the original and Laplacian images
cv2.imshow('Original Image', image)
cv2.imshow('Laplacian Image', laplacian_abs)
cv2.waitKey(0)
cv2.destroyAllWindows()
