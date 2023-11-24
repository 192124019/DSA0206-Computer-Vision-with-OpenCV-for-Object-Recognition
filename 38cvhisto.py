import cv2
import numpy as np
import matplotlib.pyplot as plt

def analyze_image_histogram(image_path):
    # Read the image
    image = cv2.imread(r"C:\Users\USER\Downloads\APTOPIX_Emirates_Asia_Cup_Cricket_83462.jpg-96d12.jpg")

    # Convert the image to RGB (OpenCV uses BGR by default)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Calculate the histogram for each color channel
    hist_red = cv2.calcHist([image], [0], None, [256], [0, 256])
    hist_green = cv2.calcHist([image], [1], None, [256], [0, 256])
    hist_blue = cv2.calcHist([image], [2], None, [256], [0, 256])

    # Plot the histograms
    plt.figure(figsize=(12, 6))

    plt.subplot(131)
    plt.plot(hist_red, color='red')
    plt.title('Red Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')

    plt.subplot(132)
    plt.plot(hist_green, color='green')
    plt.title('Green Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')

    plt.subplot(133)
    plt.plot(hist_blue, color='blue')
    plt.title('Blue Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')

    plt.tight_layout()
    plt.show()

# Specify the path to the image
image_path = 'path/to/your/image.jpg'

# Call the function to analyze the histogram
analyze_image_histogram(image_path)
