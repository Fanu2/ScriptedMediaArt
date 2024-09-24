from PIL import Image, ImageDraw
import os

# Define paths
image_paths = [
    "/home/jasvir/Music/circular/5.png",
    "/home/jasvir/Music/circular/6.png"
]
output_path = "/home/jasvir/Music/circular/composite.png"
radius = 200  # Radius for the circular crop


def create_circular_image(image_path, output_path, radius):
    """Create a circular image from the given image path and save it."""
    with Image.open(image_path) as img:
        # Create a mask for the circular area
        mask = Image.new('L', (radius * 2, radius * 2), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, radius * 2, radius * 2), fill=255)

        # Resize image to fit within the circle
        img = img.resize((radius * 2, radius * 2), Image.Resampling.LANCZOS)
        img.putalpha(mask)

        # Save circular image
        img.save(output_path, format='PNG')


def create_composite_image(image_paths, output_path):
    """Create a composite image from the list of image paths."""
    images = [Image.open(p) for p in image_paths]

    # Create a new image for the composite
    composite_width = sum(img.width for img in images)
    composite_height = max(img.height for img in images)
    composite = Image.new('RGBA', (composite_width, composite_height))

    # Paste images onto the composite image
    x_offset = 0
    for img in images:
        composite.paste(img, (x_offset, 0), img)
        x_offset += img.width

    composite.save(output_path, format='PNG')


# Paths for circular images
circular_image_paths = [
    "/home/jasvir/Music/circular/1_circular.png",
    "/home/jasvir/Music/circular/2_circular.png"
]

# Create circular images
for i, image_path in enumerate(image_paths):
    create_circular_image(image_path, circular_image_paths[i], radius)

# Create composite image
create_composite_image(circular_image_paths, output_path)

print("Composite image created successfully!")
