from wand.image import Image

def apply_decorate(input_path, output_path):
    with Image(filename=input_path) as img:
        # Add a black border to the image
        img.border(color='black', width=20, height=20)
        # Save the image with the border applied
        img.save(filename=output_path)

# Example usage
input_image_path = '/home/jasvir/Pictures/Decorate/jas.jpg'
output_image_path = '/home/jasvir/Pictures/Decorate/jas1.jpg'
apply_decorate(input_image_path, output_image_path)
