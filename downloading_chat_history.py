import os

# URL of the webpage
url = "https://chatgpt.com/share/ccacce33-abf0-4789-867a-e4c1bb1e22b3"
output_path = "/home/jasvir/Documents/chtgpt/"

# Use wget command to save the entire webpage
os.system(f"wget --mirror --convert-links --adjust-extension --page-requisites --no-parent -P {output_path} {url}")

print("Webpage saved successfully.")
