import cv2

# Load the pre-trained Haarcascade classifier for face detection
face_cascade = cv2.CascadeClassifier(r"C:\Users\Lenovo\Documents\Praxis_AI\03-02-Haarcascade\haarcascade_frontalface_default.xml")

# Capture video from the webcam
cap = cv2.VideoCapture(0)

while True:
    # Read frame from the webcam
    ret, frame = cap.read()

    if not ret:
        break

    # Resize the frame to make processing faster
    resized = cv2.resize(frame, (480, 360))

    # Convert the frame to grayscale
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, 6.5, 17)  # You can tune these parameters

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(resized, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the frame with the detected faces
    cv2.imshow('Webcam Face Detection', resized)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the display window
cap.release()
cv2.destroyAllWindows()
