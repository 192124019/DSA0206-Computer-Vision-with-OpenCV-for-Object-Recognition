# Import the library
import cv2

# Read the image
image = cv2.imread(r"C:\Users\USER\Downloads\394091-1670218124.jpg")

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Load the pre-trained Haar cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(r"C:\Users\USER\Downloads\haarcascade_frontalface_default.xml")

# Apply the classifier to the grayscale image
faces = face_cascade.detectMultiScale(gray_image, 1.3, 5)

# Draw a rectangle around the detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display and save the modified image
cv2.imshow("Face Detection", image)
cv2.imwrite("face_detection.jpg", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Count the number of faces detected
face_count = len(faces)
print("Number of faces detected:1", face_count)
