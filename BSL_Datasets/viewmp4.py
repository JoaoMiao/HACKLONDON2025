import cv2

video_path = "/Users/joaomiao/BSL_Datasets/Hello.mp4"

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video file.")
else:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Playback", frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):  # Press 'q' to close
            break

    cap.release()
    cv2.destroyAllWindows()
