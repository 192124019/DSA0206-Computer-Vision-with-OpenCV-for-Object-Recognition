import cv2

# Read input image
img = cv2.imread(r"C:\Users\USER\Downloads\394091-1670218124.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Use full paths to Haar cascade XML files
face_cascade = cv2.CascadeClassifier(r"C:\Users\USER\Downloads\haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(r"C:\Users\USER\Downloads\haarcascade_eye_tree_eyeglasses.xml")

# Detect faces in the input image
faces = face_cascade.detectMultiScale(gray, 1.3, 4)
print('Number of detected faces:', len(faces))

# Loop over the detected faces
for (x, y, w, h) in faces:
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

    # Detect eyes within the detected face area (roi)
    eyes = eye_cascade.detectMultiScale(roi_gray)

    # Draw a rectangle around eyes
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 255), 2)

# Display the image with detected eyes
cv2.imshow('Eyes Detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
