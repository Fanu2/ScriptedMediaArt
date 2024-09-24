from PIL import Image, ImageDraw, ImageFont
import os
import re

# Define paths
input_file = "/home/jasvir/Music/jodha1/Jodha_hindi/new_file.txt"
output_dir = "/home/jasvir/Music/jodha1/Jodha_hindi/images/"
font_path = "/usr/share/fonts/truetype/noto/NotoSansDevanagari-Regular.ttf"  # Ensure this path is correct
font_size = 24
image_width = 800
image_height = 600

# Read the entire content from the input file
with open(input_file, "r", encoding="utf-8") as file:
    content = file.read()

# Extract sentences enclosed in double quotes
sentences = re.findall(r'"(.*?)"', content)

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Load the font
try:
    font = ImageFont.truetype(font_path, font_size)
except IOError:
    print(f"Font file not found: {font_path}")
    exit()

# Create images for each sentence
for i, sentence in enumerate(sentences):
    # Create a new image with white background
    image = Image.new('RGB', (image_width, image_height), 'white')
    draw = ImageDraw.Draw(image)

    # Calculate text size using textbbox
    bbox = draw.textbbox((0, 0), sentence, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Print debugging information
    print(f"Processing sentence {i + 1}:")
    print(f"Text: {sentence}")
    print(f"Bounding Box: {bbox}")
    print(f"Text Width: {text_width}, Text Height: {text_height}")

    # Calculate position for centering text
    text_x = (image_width - text_width) / 2
    text_y = (image_height - text_height) / 2

    # Draw the text
    draw.text((text_x, text_y), sentence, font=font, fill='black')

    # Save image
    image_filename = os.path.join(output_dir, f"sentence_{i + 1}.png")
    image.save(image_filename)

    print(f"Image saved: {image_filename}")

print("All images created successfully!")
