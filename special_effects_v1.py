
from wand.image import Image

def apply_special_effects(input_path, output_path):
    with Image(filename=input_path) as img:
        img.charcoal(radius=2, sigma=1)
        img.save(filename=output_path)

# Example usage
apply_special_effects('input.jpg', 'output.jpg')
