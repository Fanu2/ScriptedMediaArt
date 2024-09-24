from wand.image import Image

def apply_composite(image1_path, image2_path, output_path):
    # Open the first image
    with Image(filename=image1_path) as img1:
        # Open the second image
        with Image(filename=image2_path) as img2:
            # Resize the second image if it's larger than the first image
            if img2.width > img1.width or img2.height > img1.height:
                img2.resize(img1.width, img1.height)

            # Composite the second image onto the first image
            img1.composite(img2, left=150, top=150)
            # Save the result to the specified path
            img1.save(filename=output_path)

# Example usage
image1_path = '/home/jasvir/Pictures/Composite/1.jpg'
image2_path = '/home/jasvir/Pictures/Composite/2.png'
output_path = '/home/jasvir/Pictures/Composite/output.jpg'
apply_composite(image1_path, image2_path, output_path)
