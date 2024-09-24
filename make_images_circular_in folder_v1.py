from PIL import Image, ImageDraw, ImageOps
import os


def make_circular(input_directory, output_directory):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Get all files in the input directory
    files = [f for f in os.listdir(input_directory) if os.path.isfile(os.path.join(input_directory, f))]

    for file in files:
        # Open the image
        img_path = os.path.join(input_directory, file)
        img = Image.open(img_path).convert("RGBA")

        # Create a circular mask
        mask = Image.new("L", img.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + img.size, fill=255)

        # Apply the circular mask to the image
        circular_img = Image.new("RGBA", img.size)
        circular_img.paste(img, (0, 0), mask=mask)

        # Save the circular image to the output directory
        output_path = os.path.join(output_directory, file)
        circular_img.save(output_path, format="PNG")

    print(f"Circular images saved in {output_directory}")


# Set the input and output directory paths
input_directory = "/home/jasvir/Music/jodha1/Jodha_hindi/images/"
output_directory = "/home/jasvir/Music/jodha1/Jodha_hindi/images/jodha1_circular/"

# Call the function
make_circular(input_directory, output_directory)
