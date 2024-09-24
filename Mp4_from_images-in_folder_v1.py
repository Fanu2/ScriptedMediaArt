from moviepy.editor import ImageSequenceClip
import os

# Define the path to the folder containing the images
image_folder = "/home/jasvir/Music/Jodha3/images/circular/combined_images/"
output_file = "/home/jasvir/Music/Jodha3/images/circular/combined_images/video.mp4"

# List all images in the folder
image_files = [os.path.join(image_folder, img) for img in sorted(os.listdir(image_folder)) if img.endswith(('png', 'jpg', 'jpeg'))]

# Check if there are any images in the folder
if not image_files:
    raise ValueError("No images found in the folder.")

# Create an ImageSequenceClip object with each image appearing for 10 seconds
# Set fps to a suitable value (e.g., 24 fps)
fps = 4/10
clip = ImageSequenceClip(image_files, fps=fps)

# Write the video file
clip.write_videofile(output_file, codec='libx264')

print("Video created successfully!")
