import subprocess
import os


def create_video(image_file, audio_file, subtitle_file, output_video):
    try:
        # Ensure the output directory exists
        output_dir = os.path.dirname(output_video)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Step 1: Create a video from the image and audio
        temp_video = "temp_video.mp4"
        ffmpeg_image_audio_command = [
            "ffmpeg",
            "-y",  # Automatically overwrite existing files
            "-loop", "1",
            "-i", image_file,
            "-i", audio_file,
            "-c:v", "libx264",
            "-tune", "stillimage",
            "-c:a", "aac",
            "-b:a", "192k",
            "-pix_fmt", "yuv420p",
            "-shortest",
            "-vf", "scale=1280:720",
            temp_video
        ]

        subprocess.run(ffmpeg_image_audio_command, check=True)

        # Step 2: Add subtitles with custom styling (green text with background)
        ffmpeg_subtitle_command = [
            "ffmpeg",
            "-y",  # Automatically overwrite existing files
            "-i", temp_video,
            "-vf",
            f"subtitles={subtitle_file}:force_style='Fontsize=24,PrimaryColour=&H00FF00&,BackColour=&H80000000&,BorderStyle=3,Alignment=2'",
            "-c:a", "copy",
            output_video
        ]

        subprocess.run(ffmpeg_subtitle_command, check=True)

        # Step 3: Clean up temporary video file
        os.remove(temp_video)

        print(f"Video created successfully: {output_video}")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred during the FFmpeg process: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    image_file = "/home/jasvir/Music/jodha8/1.png"
    audio_file = "/home/jasvir/Music/jodha8/1.mp3"
    subtitle_file = "/home/jasvir/Music/jodha8/1.srt"
    output_video = "/home/jasvir/Music/jodha8/jodha.mp4"

    # Create the video
    create_video(image_file, audio_file, subtitle_file, output_video)
