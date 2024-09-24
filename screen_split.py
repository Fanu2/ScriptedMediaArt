import numpy as np
from moviepy.editor import VideoFileClip, CompositeVideoClip, ImageClip

# Duration for each scene
duration = 6  # seconds

# Load the main video clip
main_clip = VideoFileClip("/home/jasvir/Music/jodha6/2.mp4")
W, H = main_clip.size

# Function to create a split mask with reduced masked area
def create_mask(x_start, x_end, H, color_1, color_2):
    mask_width = (x_end - x_start) // 2  # Reduce the mask width to half
    mask = np.zeros((H, mask_width, 3), dtype=np.uint8)
    mask[:, :mask_width // 2] = color_1
    mask[:, mask_width // 2:] = color_2
    return mask

# Convert numpy array mask to ImageClip
def mask_to_clip(mask_array):
    # Convert numpy array to a suitable format for ImageClip
    mask_image = np.uint8(mask_array)
    return ImageClip(mask_image, ismask=True).set_duration(1)

# Create left clip with reduced mask area
left_mask_array = create_mask(W // 3, 2 * W // 3, H, color_1=[255, 255, 255], color_2=[0, 0, 0])
left_mask_clip = mask_to_clip(left_mask_array)

clip_left = (
    main_clip.subclip(0, duration)
    .crop(x1=W // 3, x2=W // 3 + (W // 3 // 2))  # Crop with reduced width
    .set_mask(left_mask_clip)
)

# Create right clip with reduced mask area
right_mask_array = create_mask(0, W // 3 + 2, H, color_1=[0, 0, 0], color_2=[255, 255, 255])
right_mask_clip = mask_to_clip(right_mask_array)

clip_right = (
    main_clip.subclip(21, 21 + duration)
    .crop(x1=W // 3, x2=W // 3 + (W // 3 // 2))  # Crop with reduced width
    .set_mask(right_mask_clip)
)

# Assemble the final video
final_clip = CompositeVideoClip(
    [
        clip_left.set_position("left").set_audio(None),
        clip_right.set_position("right").set_audio(None),
    ],
    size=(W, H)
)

# Output the final video
output_path = "/home/jasvir/Music/jodha6/jodha_my_love_reduced.avi"
final_clip.write_videofile(output_path, fps=24, codec="mpeg4")

print(f"Final video saved to {output_path}")
