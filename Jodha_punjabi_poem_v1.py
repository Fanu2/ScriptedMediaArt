import os
import random
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import ImageSequenceClip, AudioFileClip

# Paths
poem_text = [
    "ਜੌਧਾ, ਤੇਰੀਆਂ ਅੱਖਾਂ 'ਚ ਪਿਆਰ ਦੇ ਸਾਗਰ ਹਨ,\nਤੇਰੇ ਬਿਨਾ ਦਿਲ ਬੇਚੈਨ ਹੈ।",
    "ਜੌਧਾ, ਤੇਰੇ ਨਾਲ ਇਹ ਜ਼ਿੰਦਗੀ ਸੋਹਣੀ ਹੈ,\nਤੇਰੇ ਬਿਨਾ ਇਹ ਦਿਲ ਉਦਾਸ ਹੈ।",
    "ਜੌਧਾ, ਤੇਰੀ ਹੱਸੀ 'ਚ ਸਵਰਗ ਦਾ ਅਹਿਸਾਸ ਹੈ,\nਤੇਰੇ ਬਿਨਾ ਸਭ ਕੁਝ ਸੁੰਨਾ ਹੈ।",
    "ਜੌਧਾ, ਤੇਰੇ ਬਿਨਾ ਇਹ ਦੁਨੀਆ ਅਧੂਰੀ ਹੈ,\nਤੇਰੇ ਨਾਲ ਹਰ ਪਲ ਪੂਰਾ ਹੈ।",
    "ਜੌਧਾ, ਤੇਰੇ ਬਿਨਾ ਸਪਨਿਆਂ ਵਿੱਚ ਵੀ ਚੈਨ ਨਹੀਂ,\nਤੇਰੇ ਨਾਲ ਦਿਲ ਨੂੰ ਮਿਲਦਾ ਹੈ ਸੁਕੂਨ।",
    "ਜੌਧਾ, ਤੇਰੇ ਬਿਨਾ ਸਭ ਕੁਝ ਖਾਲੀ ਖਾਲੀ ਹੈ,\nਤੇਰੇ ਨਾਲ ਹਰ ਲਹਿਰ ਰੰਗੀਨ ਹੈ।",
    "ਜੌਧਾ, ਤੇਰੇ ਬਿਨਾ ਇਹ ਧੜਕਣ ਨਹੀਂ ਚੱਲਦੀ,\nਤੇਰੇ ਨਾਲ ਇਹ ਜ਼ਿੰਦਗੀ ਇਕ ਕਿਤਾਬ ਹੈ।",
    "ਜੌਧਾ, ਤੇਰੇ ਪਿਆਰ ਵਿੱਚ ਦਿਲ ਦਾ ਸੁਰੂਰ ਹੈ,\nਤੇਰੇ ਬਿਨਾ ਹਰ ਖੁਸ਼ੀ ਹੈ ਗੁੰਮਨਾਮ ਅਤੇ ਅਧੂਰੀ।"
]
output_dir = "/home/jasvir/Pictures/Jodha Poem 4/"
audio_path = "/home/jasvir/Pictures/Jodha Poem 4/1.mp3"
output_video = "/home/jasvir/Pictures/Jodha Poem 4/Love you Jodha 4.mp4"
font_path = "/usr/share/fonts/truetype/lohit-punjabi/Lohit-Gurmukhi.ttf"
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
