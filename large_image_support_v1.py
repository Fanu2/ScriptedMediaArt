
from wand.image import Image

def apply_large_image_support(input_path, output_path):
    with Image(filename=input_path) as img:
        img.sample(width=img.width // 2, height=img.height // 2)
        img.save(filename=output_path)

# Example usage
apply_large_image_support('input.jpg', 'output.jpg')
