import os
import time

def convert_to_srt(input_file, output_file, sentence_duration):
    """
    Convert a text file to an SRT subtitle file.

    :param input_file: Path to the input text file
    :param output_file: Path to the output SRT file
    :param sentence_duration: Duration of each sentence in seconds
    """
    # Read the input file
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
        return
    except Exception as e:
        print(f"Error: Unable to read the file. {str(e)}")
        return

    # Initialize the SRT output
    srt_output = ''
    timestamp = 0

    # Loop through the lines and generate the SRT format
    for i, line in enumerate(lines):
        # Skip empty lines
        if not line.strip():
            continue

        # Format the start and end timestamps
        start_time = time.strftime('%H:%M:%S,000', time.gmtime(timestamp))
        end_time = time.strftime('%H:%M:%S,000', time.gmtime(timestamp + sentence_duration))
        timestamp += sentence_duration

        # Add the SRT formatted output
        srt_output += f"{i + 1}\n"
        srt_output += f"{start_time} --> {end_time}\n"
        srt_output += f"{line.strip()}\n\n"

    # Write the SRT output to the file
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(srt_output)
        print(f"SRT file generated: {output_file}")
    except Exception as e:
        print(f"Error: Unable to write to the file. {str(e)}")

if __name__ == "__main__":
    # Hardcoded input and output paths
    input_file = '/home/jasvir/Music/jodha9/jodha.txt'  # Change this to your input file path
    output_file = '//home/jasvir/Music/jodha9/output.srt'  # Change this to your output file path

    # Sentence duration in seconds (you can also change this if needed)
    sentence_duration = 5  # Change this to adjust sentence duration

    # Call the convert_to_srt function
    convert_to_srt(input_file, output_file, sentence_duration)
