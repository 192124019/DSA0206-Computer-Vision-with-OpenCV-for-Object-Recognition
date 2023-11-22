import cv2
import numpy as np

def apply_sobel(input_image_path):
    # Read the input image
    input_image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)

    if input_image is None:
        print(f"Error: Could not read the image at '{input_image_path}'")
        return

    # Apply the Sobel filter in the x and y directions
    sobel_x = cv2.Sobel(input_image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(input_image, cv2.CV_64F, 0, 1, ksize=3)

    # Combine the x and y gradients to obtain the magnitude
    sobel_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)

    # Normalize the magnitude to the range [0, 255]
    sobel_magnitude = np.uint8(255 * sobel_magnitude / np.max(sobel_magnitude))

    # Display the original and Sobel-filtered images
    cv2.imshow("Original Image", input_image)
    cv2.imshow("Sobel X", cv2.convertScaleAbs(sobel_x))
    cv2.imshow("Sobel Y", cv2.convertScaleAbs(sobel_y))
    cv2.imshow("Sobel Magnitude", sobel_magnitude)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage: Apply Sobel filter to an image
input_image_path = "C:/Users/USER/Downloads/394091-1670218124.jpg"  # Replace with the actual path to your image
apply_sobel(input_image_path)
