import cv2
import numpy as np

def overlay_text_on_image(image_path, text):
    # Read the image
    image = cv2.imread(r"C:\Users\USER\Downloads\APTOPIX_Emirates_Asia_Cup_Cricket_83462.jpg-96d12.jpg")

    # Define the font, scale, and color
    font = cv2.FONT_HERSHEY_SIMPLEX
    scale = 5
    color = (0, 0, 255)  # White color

    # Get the size of the text
    text_size = cv2.getTextSize(text, font, scale, 1)[0]

    # Calculate the position to center the text on the image
    text_x = (image.shape[1] - text_size[0]) // 2
    text_y = (image.shape[0] + text_size[1]) // 2

    # Overlay the text on the image
    cv2.putText(image, text, (text_x, text_y), font, scale, color, 1, cv2.LINE_AA)

    # Display the image with the overlaid text
    cv2.imshow('Image with Text', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the image with the overlaid text
    output_path = 'output_image.jpg'
    cv2.imwrite(output_path, image)

    print(f"Image with text overlay saved at: {output_path}")

# Get user input for the text
user_text = input("Enter the text to be overlaid on the image: ")

# Specify the path to the image
image_path = 'path/to/your/image.jpg'

# Call the function to overlay the text on the image
overlay_text_on_image(image_path, user_text)
