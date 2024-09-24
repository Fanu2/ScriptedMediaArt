from moviepy.editor import ImageSequenceClip, concatenate_videoclips
from PIL import Image
import os
import numpy as np

# Define paths
images_folder1 = "/home/jasvir/Music/jodha1/Jodha_hindi/images/jodha1_circular/"
images_folder2 = "/home/jasvir/Music/jodha1/Jodha_hindi/images2/circular/"
output_video_path = "/home/jasvir/Music/jodha1/Jodha_hindi/page_turn_video.mp4"
frame_duration = 1  # Duration of each frame in seconds

def resize_images(image1, image2):
    """Resize images to the same dimensions."""
    width1, height1 = image1.size
    width2, height2 = image2.size
    new_width = min(width1, width2)
    new_height = min(height1, height2)

    image1 = image1.resize((new_width, new_height))
    image2 = image2.resize((new_width, new_height))

    return image1, image2

def apply_page_turn_effect(image1, image2):
    """Create a page-turning effect between two images."""
    frames = []
    num_frames = 15
    for i in range(num_frames):
        alpha = i / (num_frames - 1)
        blended_image = Image.blend(image1, image2, alpha)
        frames.append(np.array(blended_image))  # Convert PIL image to NumPy array
    return frames

def create_video_from_images(folder1, folder2, output_path, frame_duration):
    """Create a video from images in two folders with page-turning effect."""
    images1 = sorted([os.path.join(folder1, f) for f in os.listdir(folder1) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])
    images2 = sorted([os.path.join(folder2, f) for f in os.listdir(folder2) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])

    if len(images1) != len(images2):
        raise ValueError("Both folders should have the same number of images.")

    all_frames = []

    for img1_path, img2_path in zip(images1, images2):
        img1 = Image.open(img1_path).convert('RGB')  # Ensure the image is in RGB mode
        img2 = Image.open(img2_path).convert('RGB')
        img1, img2 = resize_images(img1, img2)
        frames = apply_page_turn_effect(img1, img2)
        all_frames.extend(frames)

    # Create video clip from NumPy arrays
    clip = ImageSequenceClip([np.array(frame) for frame in all_frames], fps=4)
    clip.write_videofile(output_path, fps=4, codec="libx264")

# Create video
create_video_from_images(images_folder1, images_folder2, output_video_path, frame_duration)
print("Video created successfully!")
