import pyperclip
import os


# Function to create the HTML file
def create_html_from_clipboard(file_name="index.html"):
    # Get data from clipboard
    clipboard_data = pyperclip.paste()

    # Basic HTML structure
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your Page Title</title>
    <style>
        /* Add custom styles here */
    </style>
</head>
<body>
    {clipboard_data}
</body>
</html>
"""

    # Save the HTML content to a file
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(html_content)

    print(f"HTML file '{file_name}' created successfully.")


# Create the HTML file in the current directory
if __name__ == "__main__":
    # Set your desired file name
    file_name = "/home/jasvir/Music/html/ED.html"
    create_html_from_clipboard(file_name)

    # Optionally, open the file in the default web browser
    os.system(f"start {file_name}")
