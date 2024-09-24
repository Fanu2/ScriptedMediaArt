
from wand.image import Image

def apply_heterogeneous_distributed_processing(input_path, output_path):
    with Image(filename=input_path) as img:
        img.enable_opencl()
        img.save(filename=output_path)

# Example usage
apply_heterogeneous_distributed_processing('input.jpg', 'output.jpg')
