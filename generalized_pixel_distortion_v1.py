
from wand.image import Image

def apply_generalized_pixel_distortion(input_path, output_path):
    with Image(filename=input_path) as img:
        img.distort('perspective', [0,0, 30,60, 100,0, 70,90, 0,100, 60,70, 100,100, 90,70])
        img.save(filename=output_path)

# Example usage
apply_generalized_pixel_distortion('input.jpg', 'output.jpg')
