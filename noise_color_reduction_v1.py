
from wand.image import Image

def apply_noise_color_reduction(input_path, output_path):
    with Image(filename=input_path) as img:
        img.noise('Kuwahara')
        img.save(filename=output_path)

# Example usage
apply_noise_color_reduction('input.jpg', 'output.jpg')
