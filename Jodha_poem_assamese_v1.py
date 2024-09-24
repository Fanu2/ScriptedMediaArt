import os
import random
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import ImageSequenceClip, AudioFileClip

# Paths
poem_text = [
    "জোধা, তোমাৰ মৰমে সজীৱ মোৰ জীৱন,\nতোমাৰ স্পৰ্শে সপোন বুনাইছে প্ৰণয়ৰ মণি।",
    "তোমাৰ হাঁহিত মিঠা পুৰাণৰ সুৰ,\nতোমাৰ সতে যোৱা বেলি, সপোনৰ কথা সুৰ।",
    "তুমি মোৰ হৃদয়ৰ আঁচলৰ প্ৰেমৰ ফুল,\nজোধা, তোমাৰ উপস্থিতি লয় উজাগৰ ৰূপ।",
    "তোমাৰ বাহুতেই পোৱা শান্তিৰ অবলম্বন,\nতোমাৰ চকুতে সপোন সৃষ্টিৰ আৰ্হি তুলি বৰ্ণ।",
    "জোধা, তোমাৰ প্ৰেমে মোৰ হৃদয়ৰ চিত্ৰ আঁকা,\nতোমাৰ নাচত অমৃতৰ সুৰ সঁচাৰ পোৱা আঁকা।",
    "এই প্ৰেমৰ জগতৰ কাহিনী আমাৰ সুখৰ ৰং,\nজোধা, তোমাৰ সতে ৰ’ব অমল আনন্দৰ সংগ।"
]
output_dir = "/home/jasvir/Pictures/Jodha Poem Assamese/"
audio_path = "/home/jasvir/Pictures/Jodha Poem Assamese/1.mp3"
output_video = "/home/jasvir/Pictures/Jodha Poem Assamese/Love you Jodha a5.mp4"
font_path = "/usr/share/fonts/truetype/lohit-assamese/Lohit-Assamese.ttf"
image_size = (720, 720)

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

# Adjust the list to match the length of the audio
audio = AudioFileClip(audio_path)
duration = audio.duration
fps = 1  # one image per second
n_images = int(duration * fps)
if len(image_files) > n_images:
    image_files = image_files[:n_images]
else:
    image_files.extend(random.choices(image_files, k=n_images - len(image_files)))

# Create video from images and audio
clip = ImageSequenceClip(image_files, fps=fps)
clip = clip.set_audio(audio)
clip.write_videofile(output_video, codec="libx264", audio_codec="aac")

print("Video created successfully!")
