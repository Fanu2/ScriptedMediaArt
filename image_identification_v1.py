
from wand.image import Image

def apply_image_identification(input_path):
    with Image(filename=input_path) as img:
        print(img.format, img.size, img.depth)

# Example usage
apply_image_identification('input.jpg')
