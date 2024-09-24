from moviepy.editor import *
from moviepy.video.fx.all import resize, crop
import numpy as np

def make_circle_mask(size, radius=None, color=1, bg_color=0):
    """Create a circular mask of a given size."""
    radius = radius or min(size) / 2
    X, Y = np.ogrid[:size[1], :size[0]]
    dist_from_center = np.sqrt((X - size[1] / 2) ** 2 + (Y - size[0] / 2) ** 2)
    mask_array = dist_from_center <= radius
    return ImageClip(color * mask_array.astype(float) + bg_color * (~mask_array).astype(float),
                     ismask=True).resize(size)

# Paths to the input videos
video_paths = [
    "/home/jasvir/Music/jodha6/1.mp4",
    "/home/jasvir/Music/jodha6/2.mp4",
    "/home/jasvir/Music/jodha6/3.mp4",
    "/home/jasvir/Music/jodha6/4.mp4"
]



# Add a title screen at the beginning
title = TextClip("Jodha my Love", fontsize=70, color='white', bg_color='black', size=(720, 480))
title = title.set_duration(3).fadein(1).fadeout(1).set_position('center')

# Add background music
background_music = AudioFileClip('/home/jasvir/Music/jodha6/jatti.mp3')



# Output the final video with higher bitrate and proper codec
output_path = "/home/jasvir/Music/jodha6/final_video_circular.mp4"
final_video.write_videofile(output_path, codec='libx264', audio_codec='aac', fps=24, bitrate='4000k')

print(f"Final video saved to {output_path}")
