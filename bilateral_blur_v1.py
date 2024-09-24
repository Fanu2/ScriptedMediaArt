from wand.image import Image

def apply_color_management(input_path, output_path):
    with Image(filename=input_path) as img:
        # Convert image to grayscale
        img.transform_colorspace('gray')
        # Save the transformed image
        img.save(filename=output_path)

# Example usage
input_image_path = '/home/jasvir/Pictures/Jodha2/1.jpg'
output_image_path = '/home/jasvir/Pictures/Jodha2/output1.jpg'

apply_color_management(input_image_path, output_image_path)
