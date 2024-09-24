
from wand.image import Image

def apply_transform(input_path, output_path):
    with Image(filename=input_path) as img:
        img.rotate(45)
        img.save(filename=output_path)

# Example usage
apply_transform('input.jpg', 'output.jpg')
