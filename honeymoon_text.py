import cv2
import numpy as np

# Load the text file
with open('/home/jasvir/Music/jodha9/jodha.txt', 'r') as file:
    lines = file.readlines()

# Set the video parameters
width, height = 800, 600
fps = 30
duration = 7  # Duration of each page in seconds
font_scale = 0.8
font_color = (0, 255, 0)  # Green color
bg_color = (0, 0, 0)  # Black background

# Create the video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('/home/jasvir/Music/jodha9/scrolling_titles.mp4', fourcc, fps, (width, height))

for i in range(0, len(lines), 2):
    # Create a blank canvas
    canvas = np.zeros((height, width, 3), dtype=np.uint8)
    canvas[:] = bg_color

    # Get the text for the first line
    text1 = lines[i].strip()

    # Wrap the first line of text
    (text1_width, text1_height), _ = cv2.getTextSize(text1, cv2.FONT_HERSHEY_SIMPLEX, font_scale, 2)
    line1_parts = []
    while text1_width > width:
        # Find the last space before the text exceeds the width
        space_idx = text1.rfind(' ', 0, int(width / font_scale))
        if space_idx == -1:
            # No more spaces, split the text at the width limit
            line1_parts.append(text1[:int(width / font_scale)])
            text1 = text1[int(width / font_scale):]
        else:
            line1_parts.append(text1[:space_idx])
            text1 = text1[space_idx + 1:]
        (text1_width, text1_height), _ = cv2.getTextSize(text1, cv2.FONT_HERSHEY_SIMPLEX, font_scale, 2)

    if text1:
        line1_parts.append(text1)

    # Get the text for the second line
    if i + 1 < len(lines):
        text2 = lines[i + 1].strip()

        # Wrap the second line of text
        (text2_width, text2_height), _ = cv2.getTextSize(text2, cv2.FONT_HERSHEY_SIMPLEX, font_scale, 2)
        line2_parts = []
        while text2_width > width:
            space_idx = text2.rfind(' ', 0, int(width / font_scale))
            if space_idx == -1:
                line2_parts.append(text2[:int(width / font_scale)])
                text2 = text2[int(width / font_scale):]
            else:
                line2_parts.append(text2[:space_idx])
                text2 = text2[space_idx + 1:]
            (text2_width, text2_height), _ = cv2.getTextSize(text2, cv2.FONT_HERSHEY_SIMPLEX, font_scale, 2)

        if text2:
            line2_parts.append(text2)
    else:
        line2_parts = []

    # Determine the vertical position of the text
    y1 = (height - (len(line1_parts) * text1_height + len(line2_parts) * text2_height)) // 2
    y2 = y1 + text1_height

    # Display the first line of text
    for j, line in enumerate(line1_parts):
        x1 = (width - cv2.getTextSize(line, cv2.FONT_HERSHEY_SIMPLEX, font_scale, 2)[0][0]) // 2
        cv2.putText(canvas, line, (x1, y1 + j * text1_height), cv2.FONT_HERSHEY_SIMPLEX, font_scale, font_color, 2)

    # Display the second line of text
    for j, line in enumerate(line2_parts):
        x2 = (width - cv2.getTextSize(line, cv2.FONT_HERSHEY_SIMPLEX, font_scale, 2)[0][0]) // 2
        cv2.putText(canvas, line, (x2, y2 + j * text2_height), cv2.FONT_HERSHEY_SIMPLEX, font_scale, font_color, 2)

    # Write the canvas to the video
    for _ in range(int(fps * duration)):
        out.write(canvas)

# Release the video writer
out.release()