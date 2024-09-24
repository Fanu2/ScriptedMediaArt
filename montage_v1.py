
from wand.image import Image
from wand.display import display

def apply_montage(input_paths, output_path):
    with Image() as img:
        img.montage(*input_paths)
        img.save(filename=output_path)

# Example usage
apply_montage(['input1.jpg', 'input2.jpg'], 'output.jpg')
