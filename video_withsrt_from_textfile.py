import cv2
import numpy as np

# Load the text file
with open('/home/jasvir/Music/jodha9/jodha.txt', 'r') as file:
    lines = file.readlines()

# Set the video parameters
width, height = 800, 600
fps = 30
duration = 7  # Duration of each line in seconds
font_scale = 1
font_color = (0, 255, 0)  # Green color
bg_color = (0, 0, 0)  # Black background

# Create the video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('/home/jasvir/Music/jodha9/scrolling_titles.mp4', fourcc, fps, (width, height))

for line in lines:
    # Create a blank canvas
    canvas = np.zeros((height, width, 3), dtype=np.uint8)
    canvas[:] = bg_color

    # Get the text dimensions
    text = line.strip()
    (text_width, text_height), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, font_scale, 2)

    # Wrap the text onto multiple lines if necessary
    lines_of_text = []
    while text_width > width:
        # Split the text into two parts, the part that fits on the screen and the rest
        fit_text = text[:int(len(text) * width / text_width)]
        remaining_text = text[int(len(text) * width / text_width):]
        lines_of_text.append(fit_text)
        text = remaining_text
        (text_width, text_height), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, font_scale, 2)
    if text:
        lines_of_text.append(text)

    # Display the text on the canvas
    y = (height - len(lines_of_text) * text_height) // 2
    for line in lines_of_text:
        (text_width, text_height), _ = cv2.getTextSize(line, cv2.FONT_HERSHEY_SIMPLEX, font_scale, 2)
        x = (width - text_width) // 2
        cv2.putText(canvas, line, (x, y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, font_color, 2)
        y += text_height

    # Write the canvas to the video
    for _ in range(int(fps * duration)):
        out.write(canvas)

# Release the video writer
out.release()