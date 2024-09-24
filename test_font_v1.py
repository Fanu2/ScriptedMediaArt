from PIL import Image, ImageDraw, ImageFont

# Paths
output_dir = "/home/jasvir/Music/Jodha/"
font_path = "/usr/share/fonts/truetype/noto/NotoSansDevanagari-Regular.ttf"  # Update to the correct path
font_size = 50
image_width = 800
image_height = 600

# Sample Hindi text
text = "जोधा की सुंदरता एक खिलते हुए कमल की तरह मन को मोह लेती है."

# Create image
image = Image.new('RGB', (image_width, image_height), 'white')
draw = ImageDraw.Draw(image)

# Load the font
font = ImageFont.truetype(font_path, font_size)

# Calculate text size and position
text_width, text_height = draw.textbbox((0, 0), text, font=font)[2:]
text_x = (image_width - text_width) / 2
text_y = (image_height - text_height) / 2

# Draw text
draw.text((text_x, text_y), text, font=font, fill='black')

# Save image
image.save(os.path.join(output_dir, "test_hindi_text.png"))

print("Test image created successfully!")
