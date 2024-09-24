from moviepy.editor import VideoFileClip, AudioFileClip

# Define paths
video_path = "/home/jasvir/Music/jodha2/1.mp4"
audio_path = "/home/jasvir/Music/jodha2/1.mp3"
output_path = "/home/jasvir/Music/jodha2/output_video.mp4"


def add_audio_to_video(video_path, audio_path, output_path):
    """Add an MP3 audio track to an existing MP4 video."""
    # Load the video
    video_clip = VideoFileClip(video_path)

    # Load the audio
    audio_clip = AudioFileClip(audio_path)

    # Set the audio of the video to the new audio
    video_with_audio = video_clip.set_audio(audio_clip)

    # Write the result to a new file
    video_with_audio.write_videofile(output_path, codec="libx264", audio_codec="aac")


# Run the function
add_audio_to_video(video_path, audio_path, output_path)

print("Video with new audio created successfully!")
