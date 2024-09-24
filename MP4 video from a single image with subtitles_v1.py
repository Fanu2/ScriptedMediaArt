import subprocess
import os


def create_video_from_image(image_path, audio_path, subtitle_path, output_path):
    # Get the duration of the audio file
    command_get_duration = [
        'ffprobe',
        '-v', 'error',
        '-show_entries', 'format=duration',
        '-of', 'default=noprint_wrappers=1:nokey=1',
        audio_path
    ]

    try:
        print(f"Running command to get audio duration: {' '.join(command_get_duration)}")
        result = subprocess.run(command_get_duration, check=True, text=True, capture_output=True)
        audio_duration = float(result.stdout.strip())
        print(f"Audio duration: {audio_duration} seconds")
    except subprocess.CalledProcessError as e:
        print("An error occurred while getting the audio duration:")
        print("Output:", e.stdout)
        print("Error:", e.stderr)
        return

    # Generate video from image with the same duration as the audio
    intermediate_video_path = output_path.replace('.mp4', '_intermediate.mp4')
    command_image_to_video = [
        'ffmpeg',
        '-loop', '1',
        '-i', image_path,
        '-c:v', 'libx264',
        '-t', str(audio_duration),
        '-pix_fmt', 'yuv420p',
        '-vf', 'scale=1920:1080',  # Adjust resolution if needed
        '-y',  # Overwrite output file if it exists
        intermediate_video_path
    ]

    try:
        print(f"Running command to create video from image: {' '.join(command_image_to_video)}")
        subprocess.run(command_image_to_video, check=True, text=True, capture_output=True)
        print("Video created from image successfully.")
    except subprocess.CalledProcessError as e:
        print("An error occurred while creating the video from image:")
        print("Output:", e.stdout)
        print("Error:", e.stderr)
        return

    # Add audio and subtitles to the video
    command_add_audio_subtitles = [
        'ffmpeg',
        '-i', intermediate_video_path,
        '-i', audio_path,
        '-c:v', 'libx264',
        '-c:a', 'aac',
        '-strict', 'experimental',
        '-shortest',
        '-vf', f'subtitles={subtitle_path}',
        '-y',  # Overwrite output file if it exists
        output_path
    ]

    try:
        print(f"Running command to add audio and subtitles: {' '.join(command_add_audio_subtitles)}")
        subprocess.run(command_add_audio_subtitles, check=True, text=True, capture_output=True)
        print("MP4 file created successfully.")
    except subprocess.CalledProcessError as e:
        print("An error occurred while adding audio and subtitles:")
        print("Output:", e.stdout)
        print("Error:", e.stderr)

    # Remove intermediate video file
    try:
        os.remove(intermediate_video_path)
        print("Intermediate video file removed.")
    except OSError as e:
        print(f"Error removing intermediate video file: {e.strerror}")


# Example usage
image_path = '/home/jasvir/Pictures/fanu/1.jpg'
audio_path = '/home/jasvir/Pictures/fanu/1.mp3'
subtitle_path = '/home/jasvir/Pictures/fanu/roses_poem.srt'
output_path = '/home/jasvir/Pictures/fanu/1_with_subtitles.mp4'

create_video_from_image(image_path, audio_path, subtitle_path, output_path)
