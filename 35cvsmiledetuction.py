import cv2

# Load the pre-trained Haar cascades
face_cascade = cv2.CascadeClassifier(r'C:\Users\USER\Downloads\haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(r'C:\Users\USER\Downloads\haarcascade_smile.xml')

# Open the webcam
webcam = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    successful_frame_read, frame = webcam.read()

    if not successful_frame_read:
        break

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Draw a rectangle around the detected face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (100, 200, 50), 4)

        # Region of interest (ROI) for the detected face
        face_roi = gray_frame[y:y+h, x:x+w]

        # Detect smiles in the face ROI
        smiles = smile_cascade.detectMultiScale(face_roi, scaleFactor=1.7, minNeighbors=20)

        if len(smiles) > 0:
            # If a smile is detected, display "Smiling" text
            cv2.putText(frame, 'Smiling', (x, y+h+40), fontScale=3, fontFace=cv2.FONT_HERSHEY_PLAIN, color=(255, 255, 255))

    # Display the frame with face and smile detections
    cv2.imshow('Real-time Face and Smile Detection', frame)

    # Check for the 'Q' key to exit the loop
    key = cv2.waitKey(1)
    if key == 81 or key == 113:
        break

# Release the webcam and close all windows
webcam.release()
cv2.destroyAllWindows()
