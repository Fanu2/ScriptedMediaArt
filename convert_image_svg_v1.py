from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

# Define paths
output_dir = "/home/jasvir/Music/Jodha/"
font_path = "/usr/share/fonts/truetype/fonts-deva/NotoSansDevanagari-Regular.ttf"  # Ensure this font supports Hindi
font_size = 24
image_width = 800
image_height = 600

# Romantic lines in Hindi
lines = [
    "जोधा की सुंदरता एक खिलते हुए कमल की तरह मन को मोह लेती है.", "जोधा की आँखों में एक गहरा समुद्र है, जिसमें खो जाना अच्छा लगता है.", "जोधा के चेहरे पर मुस्कान एक सूरज की तरह चमकती है, दिल को गर्म करती है.", "जोधा की शालीनता एक पवित्र मंदिर की तरह मन को शांति देती है.", "जोधा की प्रतिबद्धता एक पहाड़ की तरह दृढ़ है, कभी नहीं डगमगाती.", "जोधा की ईमानदारी एक साफ़ पानी की तरह दिल को शुद्ध करती है.", "जोधा की निष्ठा एक दीपक की तरह जलती है, रास्ते को रोशन करती है.", "जोधा की समझदारी एक पुस्तकालय की तरह समृद्ध है, ज्ञान का भंडार है.", "जोधा की कृपा एक वर्षा की तरह शीतल है, मन को तृप्त करती है.", "जोधा की मधुर वाणी एक मधुशाला की तरह मन को लुभाती है.", "जोधा की सहनशीलता एक धरती की तरह स्थिर है, सब कुछ सहन करती है.", "जोधा की दयालुता एक वृक्ष की तरह छायादार है, सबको आश्रय देती है.", "जोधा की बुद्धि एक तेजस्वी सूर्य की तरह अज्ञानता को दूर करती है.", "जोधा की सरलता एक बच्चे की तरह निर्मल है, मन को प्रसन्न करती है.", "जोधा का आत्मविश्वास एक शेरनी की तरह सबको दम दिखाती है.", "जोधा की मेहनत एक किसान की तरह फलदार होती है.", "जोधा की सच्चाई एक हीरे की तरह चमकदार है, कभी धूमिल नहीं होती.", "जोधा की दृढ़ता एक बांध की तरह सब कुछ संभालती है.", "जोधा की प्रेमभावना एक सागर की तरह विशाल है, सबको समेट लेती है.", "जोधा एक पूर्णता की मूर्ति हैं, जिसमें सभी गुण समाहित हैं."
]

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create images
for i, line in enumerate(lines):
    # Create a new image with a white background
    image = Image.new('RGB', (image_width, image_height), 'white')
    draw = ImageDraw.Draw(image)

    # Load the font
    font = ImageFont.truetype(font_path, font_size)

    # Wrap text using textwrap
    wrapper = textwrap.TextWrapper(width=40)
    wrapped_lines = wrapper.wrap(text=line)

    # Calculate total text height using textbbox
    text_height = sum([
        draw.textbbox((0, 0), wrapped_line, font=font)[3] - draw.textbbox((0, 0), wrapped_line, font=font)[1]
        for wrapped_line in wrapped_lines
    ])

    # Calculate text position
    current_y = (image_height - text_height) / 2

    # Draw each line of text on the image
    for wrapped_line in wrapped_lines:
        text_bbox = draw.textbbox((0, 0), wrapped_line, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_x = (image_width - text_width) / 2
        draw.text((text_x, current_y), wrapped_line, font=font, fill='black')
        current_y += text_bbox[3] - text_bbox[1]

    # Save the image
    image.save(os.path.join(output_dir, f"romantic_line_{i + 1}.png"))

print("Images created successfully!")
