import cv2
import numpy as np

# Load the image
image_path = "C:/Users/USER/Downloads/images.jpg"  # Replace 'your_image_path.jpg' with the actual image file path
image = cv2.imread(image_path)

# Check if the image is loaded successfully
if image is None:
    print(f"Error: Unable to load the image at {image_path}")
else:
    # Get the height and width of the image
    height, width = image.shape[:2]

    # Define the 3D transformation matrix for a 270-degree rotation along the y-axis
    rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), 270, 1)

    # Apply the affine transformation to the image
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

    # Display the original and rotated images (optional)
    cv2.imshow('Original Image', image)
    cv2.imshow('Rotated Image', rotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the rotated image (optional)
    cv2.imwrite('rotated_image_270.jpg', rotated_image)
