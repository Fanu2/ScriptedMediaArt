
from wand.image import Image

def apply_virtual_pixel_support(input_path, output_path):
    with Image(filename=input_path) as img:
        img.virtual_pixel = 'tile'
        img.save(filename=output_path)

# Example usage
apply_virtual_pixel_support('input.jpg', 'output.jpg')
