from moviepy.editor import ColorClip, TextClip, CompositeVideoClip
from PIL import Image, ImageDraw, ImageFont
import os

# Paths and settings
image_path = '/home/jasvir/Pictures/fanu2/heart_image.png'
output_video_path = '/home/jasvir/Pictures/fanu2/get_well_soon_fanu_poem1.mp4'
font_path = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'  # Adjust path if needed
font_size = 40
text_lines = [
    "Fanu, my dear, I hope you're feeling better soon.",
    "In every moment, I think of you and send my love.",
    "The days may seem long, but soon they’ll pass.",
    "Your strength and courage will carry you through.",
    "May each sunrise bring you renewed hope.",
    "And every sunset bring you closer to health.",
    "You are a shining star, lighting up our lives.",
    "Your smile and laughter are missed so much.",
    "Take this time to rest and get well soon.",
    "Remember, you are always in my thoughts.",
    "Every beat of my heart wishes you well.",
    "May love surround you and bring you peace.",
    "Soon, you'll be back to your vibrant self.",
    "Until then, know I'm here for you always.",
    "Sending you strength, comfort, and healing.",
    "May this poem remind you of how much you are loved.",
    "Rest up, and get well, dear Fanu.",
    "You are cherished, and we can’t wait to see you healthy.",
    "Sending all my love to you each and every day.",
    "Get well soon, and come back stronger than ever.",
    "Your recovery is in my thoughts and prayers.",
    "I believe in your strength and resilience.",
    "May each new day bring you closer to health.",
    "Your well-being means the world to me.",
    "Hang in there; brighter days are ahead.",
    "You are missed, loved, and wished a speedy recovery.",
    "With every heartbeat, I’m wishing you well.",
    "Soon, we’ll see your radiant smile again.",
    "Sending hugs and warm wishes your way.",
    "Take care, and get well soon, Fanu.",
    "You are stronger than you think.",
    "We’re all rooting for your quick recovery.",
    "May you find comfort and strength in every moment."
]


def create_background_image():
    # Create a green image with a red heart in the center
    img = Image.new('RGB', (1280, 720), 'green')
    draw = ImageDraw.Draw(img)
    heart_font = ImageFont.truetype(font_path, 300)
    heart_text = "❤️"

    # Calculate position for the heart to be centered
    text_width, text_height = draw.textbbox((0, 0), heart_text, font=heart_font)[2:4]
    position = ((img.width - text_width) // 2, (img.height - text_height) // 2)

    draw.text(position, heart_text, font=heart_font, fill='red')
    img.save(image_path)


def create_video_with_subtitles():
    # Create the background image
    create_background_image()

    # Load image as color clip
    background_clip = ColorClip(size=(1280, 720), color=(0, 128, 0)).set_duration(len(text_lines) * 5)

    # Create text clips for each line
    text_clips = [
        TextClip(line, fontsize=font_size, color='white', font=font_path)
        .set_position(('center', 'bottom'))  # Change 'center' to 'bottom' for vertical position
        .set_duration(5)
        .set_start(i * 5)
        for i, line in enumerate(text_lines)
    ]

    # Combine the text clips with the background
    video = CompositeVideoClip([background_clip] + text_clips)

    # Write the result to a file
    video.write_videofile(output_video_path, fps=24)


if __name__ == '__main__':
    create_video_with_subtitles()
