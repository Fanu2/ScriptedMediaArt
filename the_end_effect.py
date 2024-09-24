from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, ImageClip
import numpy as np

# Specify the font path
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

# Function to create a fading circle mask
def create_fading_circle_mask(width, height, radius_start, radius_end, duration, t):
    # Increase the starting and ending radius to make the visible circle bigger
    radius = int(radius_start + (radius_end - radius_start) * (t / duration))
    mask = np.zeros((height, width), dtype=np.uint8)
    y, x = np.ogrid[:height, :width]
    distance = np.sqrt((x - width // 2) ** 2 + (y - height // 2) ** 2)
    mask[distance <= radius] = 255
    return mask  # Grayscale mask

# Function to generate frame with mask
def make_frame(t):
    # Increase the maximum radius value to make the circle bigger
    return create_fading_circle_mask(clip.size[0], clip.size[1], 200, 600, clip.duration, t)

# Load your video
clip = VideoFileClip("/home/jasvir/Music/jodha5/4.mp4")

# Create a mask clip from the mask array
mask_array = make_frame(0)
mask_clip = ImageClip(mask_array, ismask=True).set_duration(clip.duration).set_fps(clip.fps)

# Apply the mask to the original clip
masked_clip = clip.set_mask(mask_clip)

# Create a TextClip with a custom font
text_clip = TextClip("Love u Jodha", fontsize=70, color='white', font=font_path)

# Position the text in the center of the video
text_clip = text_clip.set_position('center').set_duration(clip.duration)

# Overlay the text on the video
final_clip = CompositeVideoClip([masked_clip, text_clip])

# Write the final video
final_clip.write_videofile("/home/jasvir/Music/jodha5/output_video1.mp4", codec="libx264", fps=24)
