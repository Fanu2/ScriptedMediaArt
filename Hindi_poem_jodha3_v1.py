import os
import random
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import ImageSequenceClip, AudioFileClip

# Paths
poem_text = [
    "तुम हो मेरी हर सुबह की पहली रोशनी,\nजोधा, तुम्हारे बिना ये दिन भी अधूरे लगते हैं।",
    "तुम्हारी बातों में छिपी हैं सतरंगी खुशियाँ,\nजोधा, तुम्हारे बिना मेरी शामें वीरान होती हैं।",
    "तुम हो मेरे सपनों की सच्चाई,\nजोधा, तुम्हारे बिना मेरी रातें तन्हा होती हैं।",
    "तुम्हारे बिना हर खुशी अधूरी है,\nजोधा, तुम्हारे साथ ही मेरी दुनिया पूरी है।",
    "तुम हो मेरी हर धड़कन का अहसास,\nजोधा, तुम्हारे बिना यह दिल भी बेजान है।",
]
output_dir = "/home/jasvir/Pictures/Jodha Poem2/"
audio_path = "/home/jasvir/Pictures/Jodha Poem2/1.mp3"
output_video = "/home/jasvir/Pictures/Jodha Poem2/Love you Jodha2.mp4"
font_path = "/usr/share/fonts/truetype/Gargi/Gargi.ttf"
image_size = (1280, 720)  # Define the size of the images

# Ensure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create poem images
for i, text in enumerate(poem_text):
    img = Image.new('RGB', image_size, color=(255, 255, 255))
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, 40)

    # Calculate text width and height
    text_bbox = d.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    d.text(((image_size[0] - text_width) / 2, (image_size[1] - text_height) / 2), text, fill=(0, 0, 0), font=font, align="center")
    img.save(os.path.join(output_dir, f"poem_{i + 1}.png"))

# Get list of all images in the folder
image_files = [os.path.join(output_dir, f) for f in os.listdir(output_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]

# Resize images to the same size
def resize_image(image_path, size):
    with Image.open(image_path) as img:
        img = img.resize(size, Image.LANCZOS)
        img.save(image_path)

for image_path in image_files:
    resize_image(image_path, image_size)

# Combine poem images and existing images alternatively
poem_images = [os.path.join(output_dir, f"poem_{i + 1}.png") for i in range(len(poem_text))]
combined_images = []
existing_images = [img for img in image_files if img not in poem_images]

for poem_img in poem_images:
    combined_images.append(poem_img)
    if existing_images:
        combined_images.append(existing_images.pop(0))

# Adjust the list to match the length of the audio
audio = AudioFileClip(audio_path)
duration = audio.duration
fps = 1  # one image per second
n_images = int(duration * fps)
if len(combined_images) > n_images:
    combined_images = combined_images[:n_images]
else:
    combined_images.extend(random.choices(combined_images, k=n_images - len(combined_images)))

# Create video from images and audio
clip = ImageSequenceClip(combined_images, fps=fps)
clip = clip.set_audio(audio)
clip.write_videofile(output_video, codec="libx264", audio_codec="aac")

print("Video created successfully!")
