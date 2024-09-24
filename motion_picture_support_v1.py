
from wand.image import Image

def apply_motion_picture_support(input_path, output_path):
    with Image(filename=input_path) as img:
        img.format = 'gif'
        img.save(filename=output_path)

# Example usage
apply_motion_picture_support('input.jpg', 'output.gif')
