from PIL import Image

# List of image paths
image_paths = [
    "/home/jasvir/Music/jas/jass/7.jpg",
    "/home/jasvir/Music/jas/jass/2.jpg",
    "/home/jasvir/Music/jas/jass/3.jpg",
    "/home/jasvir/Music/jas/jass/4.jpg",
    "/home/jasvir/Music/jas/jass/5.jpg",
    "/home/jasvir/Music/jas/jass/6.jpg"
]

# Open images
images = [Image.open(image) for image in image_paths]

# Determine the size of the collage
collage_width = max(image.width for image in images)
collage_height = sum(image.height for image in images)

# Create a blank collage image
collage = Image.new('RGB', (collage_width, collage_height))

# Paste images into the collage
y_offset = 0
for image in images:
    collage.paste(image, (0, y_offset))
    y_offset += image.height

# Save the collage
collage.save("/home/jasvir/Music/jas/jass/collage1.jpg")
