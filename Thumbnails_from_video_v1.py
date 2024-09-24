import cv2
import os


def extract_thumbnails(video_path, frame_size, output_dir):
    """
    Extracts thumbnail frames from a video at every second and saves them as image files.

    Args:
        video_path (str): The path to the input video file.
        frame_size (tuple): A tuple containing the desired dimensions (width, height) for the thumbnail frames.
        output_dir (str): The directory where the thumbnail images will be saved.

    Raises:
        Exception: If the function fails to extract frames from the video.

    The function opens the specified video file, captures frames at every second,
    resizes them to the specified dimensions, and saves them as image files with
    filenames derived from the video's base name and the timestamp.

    Example:
        extract_thumbnails('my_video.mp4', (320, 240), 'thumbnails/')

    Required Packages:
        cv2 (pip install opencv-python)

    This function is useful for generating thumbnail images from videos.
    """
    video_capture = cv2.VideoCapture(video_path)  # Open the video file for reading
    if not video_capture.isOpened():
        raise Exception(f"Cannot open video file: {video_path}")

    fps = video_capture.get(cv2.CAP_PROP_FPS)  # Get the frames per second of the video
    total_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))  # Get the total number of frames in the video
    duration = int(total_frames / fps)  # Calculate the total duration of the video in seconds

    os.makedirs(output_dir, exist_ok=True)  # Ensure the output directory exists

    for second in range(duration):
        frame_index = int(second * fps)  # Calculate the frame index for each second
        video_capture.set(cv2.CAP_PROP_POS_FRAMES, frame_index)  # Seek to the frame index
        success, frame = video_capture.read()  # Read the frame

        if success:
            frame = cv2.resize(frame, frame_size)  # Resize the frame to the specified dimensions
            thumbnail_filename = os.path.join(output_dir,
                                              f"{os.path.basename(video_path)}_thumbnail_{second}.jpg")  # Create a filename for the thumbnail
            cv2.imwrite(thumbnail_filename, frame)  # Save the thumbnail frame as an image
            print(f"Thumbnail saved to: {thumbnail_filename}")
        else:
            print(f"Could not extract frame at {second} seconds")

    video_capture.release()  # Release the video capture object


# Example usage
video_path = "/home/jasvir/Pictures/fanu/1.mp4"
frame_size = (720, 720)
output_dir = "/home/jasvir/Pictures/Thumbnails/"
extract_thumbnails(video_path, frame_size, output_dir)
