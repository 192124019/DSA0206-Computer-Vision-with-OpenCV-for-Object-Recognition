# Import OpenCV and NumPy modules
import cv2
import numpy as np

# Read the input image
image = cv2.imread(r"C:\Users\USER\Downloads\download.jpeg")

# Define the translation matrix
# For example, we want to shift the image 50 pixels to the right and 20 pixels down
tx = 50
ty = 20
transMat = np.float32([[1, 0, tx], [0, 1, ty]])

# Apply the translation
output = cv2.warpAffine(image, transMat, (image.shape[1], image.shape[0]))

# Display the output image
cv2.imshow("Output", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
