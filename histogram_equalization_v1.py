
from wand.image import Image

def apply_histogram_equalization(input_path, output_path):
    with Image(filename=input_path) as img:
        img.equalize()
        img.save(filename=output_path)

# Example usage
apply_histogram_equalization('input.jpg', 'output.jpg')
