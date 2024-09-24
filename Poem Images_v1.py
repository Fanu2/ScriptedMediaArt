from PIL import Image, ImageDraw, ImageFont
import os

# Define the poem text
poem = """
In the garden of dreams, where soft winds play,
Your smile is the dawn of a magical day.
With eyes like stars that light up the night,
You bring warmth and joy, like the sun’s golden light.

Your laughter, a melody that dances on air,
Brings a sparkle of joy, beyond compare.
In every whispered wish and every gentle touch,
You fill my heart with love, oh so much.

With every sunrise, my thoughts turn to you,
Your presence, a promise of skies so blue.
In the quiet moments and the vibrant days,
You are the muse that my heart always praises.

As petals fall softly in the evening breeze,
Your love is the comfort that puts me at ease.
In the dance of life, where our paths entwine,
Rosa, forever your heart is mine.
"""

# Define the image parameters
width, height = 800, 600
background_color = (34, 139, 34)  # Green color
text_color = (255, 255, 255)  # White color
emoticon = "❤️"  # Love emoticon

# Load a font
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Path to DejaVu Sans font
font_size = 24

# Create images with the poem text
output_dir = "/home/jasvir/Pictures/PoemImages/"
os.makedirs(output_dir, exist_ok=True)

def wrap_text(text, draw, font, max_width):
    """
    Wrap text to fit within the specified width.
    """
    lines = []
    words = text.split(' ')
    current_line = ''

    for word in words:
        test_line = f"{current_line} {word}".strip()
        text_bbox = draw.textbbox((0, 0), test_line, font=font)
        text_width = text_bbox[2] - text_bbox[0]

        if text_width <= max_width:
            current_line = test_line
        else:
            if current_line:
                lines.append(current_line)
            current_line = word

    if current_line:
        lines.append(current_line)

    return lines

def create_image(text_line, image_path):
    image = Image.new('RGB', (width, height), background_color)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, font_size)

    # Wrap the text to fit within the image width
    wrapped_text = wrap_text(text_line, draw, font, width - 40)  # 40 pixels padding

    # Calculate total text height
    line_height = font.getbbox('A')[3] - font.getbbox('A')[1] + 10  # Line height with some padding
    text_height = line_height * len(wrapped_text)

    # Calculate position for bottom-aligned text
    text_x = 20  # 20 pixels padding from left
    text_y = height - text_height - 50  # 50 pixels from the bottom

    # Draw text on the image
    for line in wrapped_text:
        draw.text((text_x, text_y), line, font=font, fill=text_color)
        text_y += line_height

    # Add emoticons
    emoticon_font_size = 48
    emoticon_font = ImageFont.truetype(font_path, emoticon_font_size)
    emoticon_bbox = draw.textbbox((0, 0), emoticon, font=emoticon_font)
    emoticon_width = emoticon_bbox[2] - emoticon_bbox[0]
    emoticon_height = emoticon_bbox[3] - emoticon_bbox[1]
    emoticon_x = (width - emoticon_width) / 2
    emoticon_y = height - emoticon_height - 20  # Adjusted to be 20 pixels from the bottom
    draw.text((emoticon_x, emoticon_y), emoticon, font=emoticon_font, fill=text_color)

    image.save(image_path)

# Split the poem into lines for creating images with one line per image
lines = poem.strip().split('\n')
for i, line in enumerate(lines):
    image_path = os.path.join(output_dir, f"poem_line_{i + 1}.png")
    create_image(line, image_path)
