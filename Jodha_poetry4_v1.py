import os
import random
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import ImageSequenceClip, AudioFileClip

# Paths
poem_text = [
    "जोधा, तुम्हारी आँखों में बसता है प्यार,\nतुम्हारे बिना दिल है बेज़ार।",
    "जोधा, तुम्हारे साथ ये जीवन है हसीन,\nतुम्हारे बिना ये दिल है ग़मगीन।",
    "जोधा, तुम्हारी हँसी में है जन्नत का अहसास,\nतुम्हारे बिना सब कुछ है उदास।",
    "जोधा, तुम्हारे बिना है ये दुनिया अधूरी,\nतुम्हारे साथ हर घड़ी है मंज़ूरी।",
    "जोधा, तुम्हारे बिना सपनों में भी नहीं चैन,\nतुम्हारे साथ दिल को मिलता है सुकून का रैन।",
    "जोधा, तुम्हारे बिना है सब सूना-सूना,\nतुम्हारे साथ हर लम्हा है रंगीन और अनोखा।",
    "जोधा, तुम्हारे बिना ये धड़कन नहीं चलती,\nतुम्हारे साथ ये ज़िंदगी है खुली किताब सी।",
    "जोधा, तुम्हारी मोहब्बत में है दिल का सुकून,\nतुम्हारे बिना हर खुशी है गुमनाम और अधूरा जुनून।"
]
output_dir = "/home/jasvir/Pictures/Jodha Poem/"
audio_path = "/home/jasvir/Pictures/Jodha Poem/1.mp3"
output_video = "/home/jasvir/Pictures/Jodha Poem/Love you Jodha4.mp4"
font_path = "/usr/share/fonts/truetype/Gargi/Gargi.ttf"
image_size = (1280, 720)

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
