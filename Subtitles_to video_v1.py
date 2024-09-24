import subprocess

def add_subtitles(video_path, subtitle_path, output_path):
    command = [
        'ffmpeg',
        '-i', video_path,
        '-vf', f'subtitles={subtitle_path}',
        '-c:a', 'copy',
        output_path
    ]

    try:
        print(f"Running command: {' '.join(command)}")
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        print("Subtitles added successfully.")
        print("Output:", result.stdout)
        print("Errors:", result.stderr)
    except subprocess.CalledProcessError as e:
        print("An error occurred while adding subtitles:")
        print("Output:", e.stdout)
        print("Error:", e.stderr)

# Example usage
video_path = '/home/jasvir/Pictures/jodha2/1.mp4'
subtitle_path = '/home/jasvir/Pictures/jodha2/romantic_poem.srt'
output_path = '/home/jasvir/Pictures/jodha2/Rani jodha .mp4'

add_subtitles(video_path, subtitle_path, output_path)
