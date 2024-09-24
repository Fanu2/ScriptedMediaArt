
from wand.image import Image

def apply_image_calculator(input_path, output_path):
    with Image(filename=input_path) as img:
        img.fx('p*0.5')
        img.save(filename=output_path)

# Example usage
apply_image_calculator('input.jpg', 'output.jpg')
