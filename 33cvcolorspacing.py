import cv2

def convert_color_space(input_image_path, output_color_space):
    # Read the input image
    input_image = cv2.imread(input_image_path)

    if input_image is None:
        print(f"Error: Could not read the image at '{input_image_path}'")
        return

    # Convert the image to the specified color space
    output_image = cv2.cvtColor(input_image, output_color_space)

    # Display the original and converted images
    cv2.imshow("Original Image", input_image)
    cv2.imshow(f"Converted to {output_color_space}", output_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage: Convert from BGR to Grayscale
input_image_path = "C:/Users/USER/Downloads/394091-1670218124.jpg"  # Replace with the actual path to your image
output_color_space = cv2.COLOR_BGR2GRAY

convert_color_space(input_image_path, output_color_space)
