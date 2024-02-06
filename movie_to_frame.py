import cv2
import os

def extract_frames(video_path, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Check if the video opened successfully
    if not cap.isOpened():
        print("Error: Unable to open video.")
        return

    frame_count = 0
    while True:
        # Read a frame from the video
        ret, frame = cap.read()

        # Break the loop if no frame is read
        if not ret:
            break

        # Save the frame as a PNG image
        frame_path = os.path.join(output_folder, f"frame_{frame_count:04d}.png")
        cv2.imwrite(frame_path, frame)

        frame_count += 1

    # Release the video capture object
    cap.release()

    print(f"Frames extracted: {frame_count}")

if __name__ == "__main__":
    video_path = "rafael.mp4"  # Path to your MP4 video file
    output_folder = "rafael_movie"  # Folder to save the extracted frames
    extract_frames(video_path, output_folder)
