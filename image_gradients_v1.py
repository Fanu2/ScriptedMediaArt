
from wand.image import Image

def apply_image_gradients(output_path):
    with Image(width=500, height=500, background='white') as img:
        img.gradient('linear', 'red', 'blue')
        img.save(filename=output_path)

# Example usage
apply_image_gradients('output.png')
