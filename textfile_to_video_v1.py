from gtts import gTTS
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips

def text_to_srt(text, duration=5):
    lines = text.split('\n')
    srt = []
    start_time = 0
    for index, line in enumerate(lines):
        start = f"00:00:{start_time:02d},000"
        end_time = start_time + duration
        end = f"00:00:{end_time:02d},000"
        srt.append(f"{index+1}\n{start} --> {end}\n{line}\n")
        start_time = end_time
    return '\n'.join(srt)

def text_to_mp3(text, mp3_filename):
    tts = gTTS(text)
    tts.save(mp3_filename)


def srt_to_images(srt_file):
    with open(srt_file, "r") as f:
        content = f.read()
    entries = content.strip().split("\n\n")

    images = []
    for index, entry in enumerate(entries):
        lines = entry.split("\n")

        # Ensure the entry has at least 3 lines
        if len(lines) < 3:
            print(f"Skipping entry {index + 1}: Not enough lines to process")
            continue

        text = lines[2]

        # Load a font, defaulting to a system-independent one if necessary
        try:
            font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
            fnt = ImageFont.truetype(font_path, 40)
        except OSError:
            fnt = ImageFont.load_default()

        img = Image.new('RGB', (800, 400), color=(73, 109, 137))
        d = ImageDraw.Draw(img)
        d.text((10, 10), text, font=fnt, fill=(255, 255, 255))
        img_name = f'image_{index + 1}.png'
        img.save(img_name)
        images.append(img_name)

    return images


def create_video_from_images_and_audio(images, audio_file, output_file):
    clips = []
    for image in images:
        clip = ImageClip(image).set_duration(5)  # 5 seconds per image
        clips.append(clip)

    video = concatenate_videoclips(clips, method="compose")
    audio = AudioFileClip(audio_file)
    video = video.set_audio(audio)
    video.write_videofile(output_file, fps=24)

# Read text from a file
with open('/home/jasvir/Music/Fanu2/fanu1.txt', 'r') as file:
    text = file.read().strip()

# Convert text to MP3
mp3_filename = "output.mp3"
text_to_mp3(text, mp3_filename)

# Convert text to SRT
srt_filename = "/home/jasvir/Music/Fanu2/subtitle.srt"
srt_content = text_to_srt(text, duration=5)
with open(srt_filename, 'w') as f:
    f.write(srt_content)

# Create images from SRT file
images = srt_to_images(srt_filename)

# Create video from images and audio
create_video_from_images_and_audio(images, mp3_filename, "/home/jasvir/Music/Fanu2/final_output.mp4")
