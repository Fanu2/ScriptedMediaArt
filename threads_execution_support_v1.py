
from wand.image import Image

def apply_threads_execution_support(input_path, output_path):
    with Image(filename=input_path) as img:
        img.threads()
        img.save(filename=output_path)

# Example usage
apply_threads_execution_support('input.jpg', 'output.jpg')
