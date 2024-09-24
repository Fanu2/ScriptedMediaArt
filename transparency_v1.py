
from wand.image import Image

def apply_transparency(input_path, output_path):
    with Image(filename=input_path) as img:
        img.alpha_channel = 'transparent'
        img.save(filename=output_path)

# Example usage
apply_transparency('input.png', 'output.png')
