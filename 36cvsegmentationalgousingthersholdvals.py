import cv2
import numpy as np

# Load the input image
input_image = cv2.imread(r"C:\Users\USER\Downloads\e8d09ff922ccee9fd8c3e247690324d2.jpg", cv2.IMREAD_GRAYSCALE)

# Check if the image is loaded successfully
if input_image is None:
    print("Error: Could not open or find the image.")
    exit()

# Set your threshold values (adjust these values accordingly)
lower_threshold = 100
upper_threshold = 255

# Apply thresholding to segment the image
_, segmented_image = cv2.threshold(input_image, lower_threshold, upper_threshold, cv2.THRESH_BINARY)

# Display the original and segmented images
cv2.imshow('Original Image', input_image)
cv2.imshow('Segmented Image', segmented_image)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
