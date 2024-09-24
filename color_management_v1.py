
from wand.image import Image

def apply_color_management(input_path, output_path):
    with Image(filename=input_path) as img:
        img.transform_colorspace('gray')
        img.save(filename=output_path)

# Example usage
apply_color_management('input.jpg', 'output.jpg')
