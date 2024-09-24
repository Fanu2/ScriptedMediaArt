from PIL import Image, ImageDraw, ImageFont
import os

# Define test paths
output_dir = "/home/jasvir/Music/jodha1/Jodha_hindi/images/"
font_path = "/usr/share/fonts/truetype/noto/NotoSansDevanagari-Regular.ttf"  # Font path
font_size = 24
image_width = 800
image_height = 600
test_text = "यह एक परीक्षण है"  # Hindi text for testing

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create a new image with white background
image = Image.new('RGB', (image_width, image_height), 'white')
draw = ImageDraw.Draw(image)

# Load the font
try:
    font = ImageFont.truetype(font_path, font_size)
except IOError:
    print(f"Font file not found: {font_path}")
    exit()

# Calculate text size using textbbox
bbox = draw.textbbox((0, 0), test_text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

# Calculate position for centering text
text_x = (image_width - text_width) / 2
text_y = (image_height - text_height) / 2

# Draw the text
draw.text((text_x, text_y), test_text, font=font, fill='black')

# Save the image
image_filename = os.path.join(output_dir, "test_image.png")
image.save(image_filename)

print(f"Test image saved: {image_filename}")
