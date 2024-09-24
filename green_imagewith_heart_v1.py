from PIL import Image, ImageDraw, ImageFont

# Image dimensions
width, height = 800, 600

# Create a green background image
image = Image.new('RGB', (width, height), 'green')
draw = ImageDraw.Draw(image)

# Define heart shape coordinates
heart_shape = [
    (width // 2, height // 3),
    (width // 2 + 100, height // 3 - 100),
    (width // 2 + 200, height // 3 + 100),
    (width // 2, height // 3 + 300),
    (width // 2 - 200, height // 3 + 100),
    (width // 2 - 100, height // 3 - 100)
]

# Draw the heart shape
draw.polygon(heart_shape, fill='red', outline='red')

# Add the text 'Love' in the center of the heart
# You need to provide the path to a TTF font file
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Update this path as needed
font_size = 60
font = ImageFont.truetype(font_path, font_size)

text = "Fanu my Love"
text_bbox = draw.textbbox((0, 0), text, font=font)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]
text_x = width // 2 - text_width // 2
text_y = height // 2 - text_height // 2

# Draw text in the center of the heart
draw.text((text_x, text_y), text, fill='white', font=font)

# Save the image
image.save('/home/jasvir/Pictures/fanu2/heart_image.png')

print('Image created and saved as heart_image.png')
