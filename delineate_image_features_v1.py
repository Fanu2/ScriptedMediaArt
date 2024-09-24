from wand.image import Image

def apply_delineate_image_features(input_path, output_path):
    with Image(filename=input_path) as img:
        # Apply Canny edge detection to the image
        img.edge(radius=1)  # Adjust radius as needed
        # Save the image with the edges delineated
        img.save(filename=output_path)

# Example usage
input_image_path = '/home/jasvir/Pictures/Delineate/fanu.jpg'
output_image_path = '/home/jasvir/Pictures/Delineate/output.jpg'
apply_delineate_image_features(input_image_path, output_image_path)
