
from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

def apply_draw(output_path):
    with Image(width=500, height=500, background=Color('white')) as img:
        with Drawing() as draw:
            draw.fill_color = Color('black')  # Set the fill color for the rectangle
            draw.rectangle(left=100, top=100, width=300, height=300)  # Draw a rectangle
            draw(img)  # Apply the drawing to the image
        img.save(filename=output_path)  # Save the image

# Example usage
apply_draw('/home/jasvir/Pictures/DFT/fanu.png')
