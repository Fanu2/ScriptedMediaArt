
from wand.image import Image

def apply_image_cache(input_path, output_path):
    with Image(filename=input_path) as img:
        img.cache()
        img.save(filename=output_path)

# Example usage
apply_image_cache('input.jpg', 'output.jpg')
