from PIL import Image, ImageDraw, ImageFont

# Parameters
image_width = 800
image_height = 600
font_size = 24
font_path = "/usr/share/fonts/truetype/noto/NotoSansDevanagari-Regular.ttf"  # Ensure this path is correct

# Create a new image with white background
image = Image.new('RGB', (image_width, image_height), 'white')
draw = ImageDraw.Draw(image)

# Load the font
try:
    font = ImageFont.truetype(font_path, font_size)
except IOError:
    print(f"Font file not found: {font_path}")
    exit()

# Define text and position
test_text = "तुम्हारी मुस्कान मेरे दिल का हर दर्द भुला देती है."
text_x = 50  # X position of text
text_y = 50  # Y position of text

# Draw text on image
draw.text((text_x, text_y), test_text, font=font, fill='black')

# Save image
output_file = "/home/jasvir/Music/jodha1/Jodha_hindi/images/test_image.png"
image.save(output_file)

print(f"Test image saved: {output_file}")
