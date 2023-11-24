import cv2
import numpy as np

def subtract_foreground(image_path, lower_bound, upper_bound):
    # Read the image
    image = cv2.imread(r"C:\Users\USER\Downloads\download (1).jpeg")

    # Convert the image to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define the color range for the foreground
    lower_bound = np.array(lower_bound, dtype=np.uint8)
    upper_bound = np.array(upper_bound, dtype=np.uint8)

    # Create a binary mask for the foreground
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Bitwise AND to extract the foreground
    result = cv2.bitwise_and(image, image, mask=mask)

    # Display the original image and the result
    cv2.imshow('Original Image', image)
    cv2.imshow('Foreground Subtraction Result', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the result
    output_path = 'foreground_subtraction_result.jpg'
    cv2.imwrite(output_path, result)

    print(f"Foreground subtraction result saved at: {output_path}")

# Specify the path to the image
image_path = 'path/to/your/image.jpg'

# Define the color range for the foreground in HSV (adjust these values)
lower_color_bound = [30, 40, 40]
upper_color_bound = [90, 255, 255]

# Call the function to subtract the foreground
subtract_foreground(image_path, lower_color_bound, upper_color_bound)
