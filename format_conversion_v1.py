
from wand.image import Image

def apply_format_conversion(input_path, output_path):
    with Image(filename=input_path) as img:
        img.format = 'jpeg'
        img.save(filename=output_path)

# Example usage
apply_format_conversion('input.png', 'output.jpg')
