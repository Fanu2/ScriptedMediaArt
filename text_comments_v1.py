
from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

def apply_text_comments(output_path):
    with Image(width=500, height=500, background=Color('white')) as img:
        with Drawing() as draw:
            draw.text(x=50, y=50, body='Hello, World!')
            draw(img)
        img.save(filename=output_path)

# Example usage
apply_text_comments('output.png')
