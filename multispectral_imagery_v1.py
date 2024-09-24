
from wand.image import Image

def apply_multispectral_imagery(input_path, output_path):
    with Image(filename=input_path) as img:
        img.format = 'tiff'
        img.save(filename=output_path)

# Example usage
apply_multispectral_imagery('input.jpg', 'output.tiff')
