# Import the libraries
import cv2
import numpy as np

# Define the function to create a white image with four colored boxes
def create_image_with_boxes(size):
    # Create a white image using np.ones() with the given size and np.uint8 data type
    image = np.ones((size, size, 3), np.uint8)
    # Multiply the image by 255 to make it fully white
    image = image * 255
    # Calculate the box size as one-tenth of the image size
    box_size = size // 10
    # Create four slices of the image corresponding to the four corners using the box size
    top_left = image[0:box_size, 0:box_size]
    top_right = image[0:box_size, -box_size:]
    bottom_left = image[-box_size:, 0:box_size]
    bottom_right = image[-box_size:, -box_size:]
    # Assign the slices to the desired colors using np.array() with the BGR values
    top_left[:] = np.array([0, 0, 0]) # black
    top_right[:] = np.array([255, 0, 0]) # blue
    bottom_left[:] = np.array([0, 255, 0]) # green
    bottom_right[:] = np.array([0, 0, 255]) # red
    # Return the modified image
    return image

# Call the function with a size of 500
result = create_image_with_boxes(500)

# Display and save the result
cv2.imshow("Result", result)
cv2.imwrite("result.jpg", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
