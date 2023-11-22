import cv2
import matplotlib.pyplot as plt

# Read the image
img = cv2.imread(r"C:\Users\USER\Downloads\APTOPIX_Emirates_Asia_Cup_Cricket_83462.jpg-96d12.jpg", cv2.IMREAD_GRAYSCALE)

# Perform histogram equalization
equ = cv2.equalizeHist(img)

# Display the original and equalized images side by side
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(equ, cmap='gray')
plt.title('Equalized Image')

plt.show()
