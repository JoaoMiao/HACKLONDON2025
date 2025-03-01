import cv2
import os

# Define the directory for saving videos
output_folder = "/Users/xuning/HACKLONDON2025/BSL_DATASETS/"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

sign_name = "Please"
video_filename = os.path.join(output_folder, f"{sign_name}.mp4")
fps = 20  # Frames per second

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Ensure camera is working
if not cap.isOpened():
    print("❌ Error: Could not open webcam.")
    exit()

# Get the actual frame size from the camera
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Use a different codec that works on macOS
fourcc = cv2.VideoWriter_fourcc(*'H264')  # Alternative codec for MP4

out = cv2.VideoWriter(video_filename, fourcc, fps, (frame_width, frame_height))

# Ensure VideoWriter initialized correctly
if not out.isOpened():
    print("❌ Error: VideoWriter not initialized correctly.")
    cap.release()
    exit()

print(f"🎥 Recording... Saving to: {video_filename}")
print("🔴 Press 'q' to stop recording.")

frame_count = 0  # Track frames recorded

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Error: Could not read frame from webcam.")
        break

    frame = cv2.flip(frame, 1)  # Flip horizontally

    # Verify frame size matches VideoWriter
    if frame.shape[1] != frame_width or frame.shape[0] != frame_height:
        print(f"⚠ Frame size mismatch: Expected ({frame_width}, {frame_height}), Got {frame.shape[1]}, {frame.shape[0]}")
        break

    out.write(frame)  # Save frame to video
    frame_count += 1

    cv2.imshow("Recording", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

# Final check if the video was saved
if os.path.exists(video_filename) and frame_count > 0:
    print(f"✅ Video successfully saved: {video_filename} ({frame_count} frames recorded)")
else:
    print("❌ Error: Video file was not created properly.")
