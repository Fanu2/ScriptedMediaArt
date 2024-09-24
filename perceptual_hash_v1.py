
from wand.image import Image

def apply_perceptual_hash(input_path):
    with Image(filename=input_path) as img:
        print(img.perceptual_hash())

# Example usage
apply_perceptual_hash('input.jpg')
