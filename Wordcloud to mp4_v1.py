#!/usr/bin/env python3

import os
from moviepy.editor import ImageClip, concatenate_videoclips, AudioFileClip
from mutagen.mp3 import MP3

# Define paths
images_dir = '/home/jasvir/Pictures/word cloud/jodha/'
audio_file = os.path.join(images_dir, '1.mp3')
output_file = os.path.join(images_dir, 'Akh Kashni.mp4')

# Get the list of image files
image_files = [os.path.join(images_dir, img) for img in os.listdir(images_dir) if img.endswith('.png')]

# Get the duration of the audio file
audio = MP3(audio_file)
audio_duration = audio.info.length

# Calculate duration per image
num_images = len(image_files)
duration_per_image = audio_duration / num_images

# Create a list of ImageClips
image_clips = [ImageClip(img).set_duration(duration_per_image) for img in image_files]

# Concatenate the image clips
video = concatenate_videoclips(image_clips, method="compose")

# Add the audio to the video
audio_clip = AudioFileClip(audio_file)
video = video.set_audio(audio_clip)

# Write the result to a file
video.write_videofile(output_file, codec="libx264", audio_codec="aac", fps=24)

print(f"Video saved to {output_file}")
