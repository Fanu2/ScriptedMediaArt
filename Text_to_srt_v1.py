from datetime import timedelta


def convert_txt_to_srt(input_path, output_path):
    # Read the text file
    with open(input_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Open the output SRT file
    with open(output_path, 'w', encoding='utf-8') as file:
        # Initialize start time
        start_time = timedelta(seconds=0)

        for index, line in enumerate(lines):
            # Remove leading/trailing whitespace
            line = line.strip()
            if not line:
                continue

            # Calculate end time (assuming each subtitle lasts 10 seconds)
            end_time = start_time + timedelta(seconds=10)

            # Format the start and end times
            start_time_str = str(start_time) + ',000'
            end_time_str = str(end_time) + ',000'

            # Write sequence number
            file.write(f"{index + 1}\n")

            # Write timecodes
            file.write(f"{start_time_str} --> {end_time_str}\n")

            # Write the subtitle text
            file.write(line + "\n\n")

            # Update start time for next subtitle
            start_time = end_time


if __name__ == "__main__":
    input_path = '/home/jasvir/Music/jodha8/jodha.txt'  # Path to your input text file
    output_path = '/home/jasvir/Music/jodha8/output1.srt'  # Path to your output SRT file
    convert_txt_to_srt(input_path, output_path)
    print(f"Converted {input_path} to {output_path} successfully.")
