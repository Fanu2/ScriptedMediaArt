import subprocess

def apply_command_line_processing(input_path, output_path):
    # Execute ImageMagick command-line tool to resize the image
    subprocess.run(['convert', input_path, '-resize', '300%', output_path])

# Example usage
input_image_path = '/home/jasvir/Pictures/Jodha2/3.jpg'
output_image_path = '/home/jasvir/Pictures/Jodha2/3b.jpg'

apply_command_line_processing(input_image_path, output_image_path)
