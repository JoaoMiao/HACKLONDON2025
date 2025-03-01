import cv2
import os

input_folder = "/Users/joaomiao/HACKLONDON2025/BSL_Datasets/"

output_folder = "BSL_Images/"
fps = 10  # Extract 5 frames per second

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for video_file in os.listdir(input_folder):
    if video_file.endswith(".mp4"):
        sign_name = video_file.split(".")[0]
        sign_folder = os.path.join(output_folder, sign_name)

        if not os.path.exists(sign_folder):
            os.makedirs(sign_folder)

        cap = cv2.VideoCapture(os.path.join(input_folder, video_file))
        frame_count = 0
        success, frame = cap.read()

        while success:
            if frame_count % (30 // fps) == 0:  # Extract every (30/fps) frames
                cv2.imwrite(f"{sign_folder}/frame_{frame_count}.jpg", frame)
            success, frame = cap.read()
            frame_count += 1

        cap.release()

print("Frames extracted successfully!")
