import os

def create_srt_from_text(text_file, srt_file, duration_per_line=10):
    with open(text_file, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file if line.strip()]

    with open(srt_file, 'w', encoding='utf-8') as file:
        start_time = 0

        for i, line in enumerate(lines, start=1):
            end_time = start_time + duration_per_line

            start_time_formatted = format_time(start_time)
            end_time_formatted = format_time(end_time)

            file.write(f"{i}\n")
            file.write(f"{start_time_formatted} --> {end_time_formatted}\n")
            file.write(f"{line}\n\n")

            start_time = end_time

def format_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    milliseconds = int((seconds - int(seconds)) * 1000)

    return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02},{milliseconds:03}"

# Example usage
text_file = '/home/jasvir/Pictures/fanu3/fanu.txt'
srt_file = '/home/jasvir/Pictures/fanu3/fanu.srt'
duration_per_line = 10  # seconds

create_srt_from_text(text_file, srt_file, duration_per_line)

print(f"SRT file created at {srt_file}")
