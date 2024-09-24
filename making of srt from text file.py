import os
import time

# Set the input and output file paths
input_file = '/home/jasvir/Music/jodha9/jodha.txt'
output_file = '/home/jasvir/Music/jodha9/jodha.srt'

# Read the input file
with open(input_file, 'r') as file:
    lines = file.readlines()

# Initialize the SRT output
srt_output = ''
timestamp = 0

# Loop through the lines and generate the SRT format
for i, line in enumerate(lines):
    # Skip empty lines
    if line.strip() == '':
        continue

    # Format the timestamp
    start_time = time.strftime('%H:%M:%S,000', time.gmtime(timestamp))
    end_time = time.strftime('%H:%M:%S,000', time.gmtime(timestamp + 7))
    timestamp += 7

    # Add the SRT format
    srt_output += f"{i + 1}\n"
    srt_output += f"{start_time} --> {end_time}\n"
    srt_output += f"{line.strip()}\n\n"

# Write the SRT output to the file
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(srt_output)

print(f"SRT file generated: {output_file}")