from wand.image import Image
from wand.sequence import Sequence


def apply_animation(input_path, output_path):
    with Image(filename=input_path) as img:
        # Create a sequence for the animation
        with Image() as gif:
            for i in range(10):
                frame = img.clone()
                frame.rotate(45 * i)  # Example transformation, rotate each frame
                gif.sequence.append(frame)

            gif.type = 'optimize'
            gif.save(filename=output_path)


# Example usage
input_image_path = '/home/jasvir/Pictures/Triza/triza.jpg'  # Replace with the actual path to your input image
output_image_path = '/home/jasvir/Pictures/Triza/output.gif'  # Replace with the desired path for your output image

apply_animation(input_image_path, output_image_path)
