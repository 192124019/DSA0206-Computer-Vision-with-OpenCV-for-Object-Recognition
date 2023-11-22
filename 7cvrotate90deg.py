import cv2
import numpy as np

# Read the image
image = cv2.imread("C:/Users/USER/Downloads/pexels-danne-516541.jpg")

# Get the dimensions of the image
height, width = image.shape[:2]

# Define the rotation matrix for a 90-degree clockwise rotation along the y-axis
rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), -90, 1)

# Perform the rotation
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

# Display the original and rotated images
#cv2.imshow('Original Image', image)
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
