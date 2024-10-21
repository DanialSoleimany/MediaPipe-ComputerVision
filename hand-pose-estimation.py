import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Start video capture
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()

    # Check if the frame was read correctly
    if not ret:
        print("Failed to grab frame. Exiting...")
        break

    # Flip the image horizontally for a mirror effect
    frame = cv2.flip(frame, 1)
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False  # Improve performance by marking the image as not writeable

    # Process the image to detect hand landmarks
    results = hands.process(image)

    # Draw the hand landmarks
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw the landmarks on the hand
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Example: Accessing specific landmark positions (like the index finger tip)
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            h, w, _ = frame.shape
            cx, cy = int(index_finger_tip.x * w), int(index_finger_tip.y * h)

            # Visualize the index finger tip
            cv2.circle(frame, (cx, cy), 10, (255, 0, 0), cv2.FILLED)
            cv2.putText(frame, 'Index Finger Tip', (cx, cy - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # Display the result
    cv2.imshow('Hand Pose Estimation', frame)

    # Exit if 'q' is pressed or the window is closed
    if cv2.waitKey(10) & 0xFF == ord('q') or cv2.getWindowProperty('Hand Pose Estimation', cv2.WND_PROP_VISIBLE) < 1:
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
