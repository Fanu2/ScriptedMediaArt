import os
from moviepy.editor import *

# Set the input and output paths
input_folder = '/home/jasvir/Music/jodha9/'
output_file = '/home/jasvir/Music/jodha9/output.mp4'
audio_file = '1.mp3'

# Get the list of PNG files in the input folder
png_files = [f for f in os.listdir(input_folder) if f.endswith('.png')]

# Create a list of video clips with the PNG images
clips = []
for i, png_file in enumerate(png_files):
    image = ImageClip(os.path.join(input_folder, png_file))
    image = image.set_position((i * 0.2, i * 0.2))
    image = image.set_duration(5)  # Set the duration of each clip to 5 seconds
    clips.append(image)

# Concatenate the clips
final_clip = concatenate_videoclips(clips, method="compose")
final_clip = final_clip.set_duration(60)  # Set the duration of the final clip to 60 seconds

# Load the audio file and set the start time to 10 seconds
audio = AudioFileClip(os.path.join(input_folder, audio_file)).set_start(10)

# Combine the video and audio clips
final_clip = final_clip.set_audio(audio)

# Write the final video to the output file
final_clip.write_videofile(output_file, fps=30, codec='libx264', preset='medium')