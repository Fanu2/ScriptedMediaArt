
from wand.image import Image

def apply_high_dynamic_range_images(input_path, output_path):
    with Image(filename=input_path) as img:
        img.high_dynamic_range()
        img.save(filename=output_path)

# Example usage
apply_high_dynamic_range_images('input.jpg', 'output.jpg')
