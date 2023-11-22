import cv2
import numpy as np

# Load the image
image = cv2.imread("C:/Users/USER/Downloads/images.jpg") 
height, width = image.shape[:2]

# Define the 3D transformation matrix for a 180-degree rotation along the y-axis
rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), 180, 1)

# Apply the affine transformation to the image
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

# Display the original and rotated images (optional)
cv2.imshow('Original Image', image)
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the rotated image (optional)
cv2.imwrite('rotated_image.jpg', rotated_image)
