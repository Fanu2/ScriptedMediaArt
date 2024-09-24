import cv2

# Open the two video files
video1 = cv2.VideoCapture('/home/jasvir/Documents/Princess Jodha/MP4/1.mp4')
video2 = cv2.VideoCapture('/home/jasvir/Documents/Princess Jodha/MP4/2.mp4')

# Get the video properties
fps1 = video1.get(cv2.CAP_PROP_FPS)
fps2 = video2.get(cv2.CAP_PROP_FPS)
width1 = int(video1.get(cv2.CAP_PROP_FRAME_WIDTH))
height1 = int(video1.get(cv2.CAP_PROP_FRAME_HEIGHT))
width2 = int(video2.get(cv2.CAP_PROP_FRAME_WIDTH))
height2 = int(video2.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Set the output video size
output_width = width1 + width2
output_height = max(height1, height2)

# Create the output video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('/home/jasvir/Music/jodha7/Two_in_one.mp4', fourcc, fps1, (output_width, output_height))

# Loop through the video frames and combine them
while True:
    ret1, frame1 = video1.read()
    ret2, frame2 = video2.read()

    if not ret1 or not ret2:
        break

    # Resize the frames to fit the output video size
    frame1 = cv2.resize(frame1, (width1, height1))
    frame2 = cv2.resize(frame2, (width2, height2))

    # Combine the frames side by side
    output_frame = cv2.hconcat([frame1, frame2])

    # Write the output frame to the video file
    out.write(output_frame)

# Release the video capture and writer objects
video1.release()
video2.release()
out.release()