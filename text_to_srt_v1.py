import re


def convert_txt_to_srt(input_file, output_file, start_time="00:00:01,000", duration_seconds=10):
    try:
        with open(input_file, 'r') as file:
            content = file.read()

        # Find all substrings within quotes (inverted commas)
        subtitles = re.findall(r'\"(.*?)\"', content)

        srt_content = []
        start_time_seconds = convert_time_to_seconds(start_time)

        for index, subtitle in enumerate(subtitles, start=1):
            subtitle = subtitle.strip()
            if subtitle:
                # Calculate start and end time for each subtitle
                end_time_seconds = start_time_seconds + duration_seconds
                start_time_srt = convert_seconds_to_time(start_time_seconds)
                end_time_srt = convert_seconds_to_time(end_time_seconds)

                # Add index, time, and subtitle text to the SRT content
                srt_content.append(f"{index}")
                srt_content.append(f"{start_time_srt} --> {end_time_srt}")
                srt_content.append(subtitle)
                srt_content.append("")  # Blank line between subtitles

                # Update start time for the next subtitle
                start_time_seconds = end_time_seconds

        # Write the SRT content to the output file
        with open(output_file, 'w') as srt_file:
            srt_file.write("\n".join(srt_content))

        # This is the corrected print statement:
        print(f"SRT file created successfully: {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")


def convert_time_to_seconds(time_str):
    h, m, s = time_str.split(':')
    s, ms = s.split(',')
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000


def convert_seconds_to_time(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int((seconds * 1000) % 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"


if __name__ == "__main__":
    input_file = "/home/jasvir/Music/jodha9/jodha.txt"
    output_file = "/home/jasvir/Music/jodha9/new_file.srt"

    # Convert the text file to SRT
    convert_txt_to_srt(input_file, output_file, start_time="00:00:01,000", duration_seconds=10)
