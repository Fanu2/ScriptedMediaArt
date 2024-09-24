from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

def apply_complex_text_layout(output_path):
    # Create a new image with white background
    with Image(width=500, height=500, background=Color('white')) as img:
        with Drawing() as draw:
            # Set font properties to use DejaVu Sans
            draw.font = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
            draw.font_size = 50
            draw.gravity = 'center'
            # Add text to the image
            draw.text(0, 0, 'Love u, Jodha!')
            # Apply the drawing to the image
            draw(img)
        # Save the image to the specified path
        img.save(filename=output_path)

# Example usage
output_image_path = '/home/jasvir/Pictures/Jodha2/output.png'
apply_complex_text_layout(output_image_path)
