import os
import random
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import ImageSequenceClip, AudioFileClip

# Poem text in Hindi
poem_text = [
    "तुम्हारे बिना यह जीवन अधूरा है,\nतुम्हारे साथ हर सपना पूरा है।",
    "तुम्हारी मुस्कान में बसी है मेरी दुनिया,\nतुम्हारे बिना मेरा हर पल सूना है।",
    "तुमसे ही है हर रंग इस जीवन में,\nतुमसे ही है हर खुशी मेरे मन में।",
    "तुम हो मेरे दिल की धड़कन,\nतुम्हारे बिना यह जीवन है वीरान।",
    "तुम्हारी हर बात मुझे भाती है,\nतुम्हारी हर हँसी मुझे लुभाती है।",
    "तुम हो मेरे जीवन का संगीत,\nतुम्हारे बिना सब कुछ है अतीत।"
]

# Paths
output_dir = "/home/jasvir/Pictures/Jodha Poem/"
audio_path = "/home/jasvir/Pictures/Jodha Poem/1.mp3"
output_video = "/home/jasvir/Pictures/Jodha Poem/Love you Jodha.mp4"
font_path = "/usr/share/fonts/truetype/Gargi/Gargi.ttf"
image_size = (1280, 720)  # Target size for all images

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
for poem_img, existing_img in zip(poem_images, image_files):
    combined_images.append(poem_img)
    combined_images.append(existing_img)

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
