import os
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def create_poetry_book(images_folder, output_pdf):
    # Get the list of all PNG images in the folder
    images = [img for img in os.listdir(images_folder) if img.endswith('.png')]
    images.sort()  # Ensure images are sorted in order

    # Set up the PDF file
    c = canvas.Canvas(output_pdf, pagesize=letter)

    for image in images:
        img_path = os.path.join(images_folder, image)
        # Open the image using Pillow
        img = Image.open(img_path)
        img_width, img_height = img.size

        # Calculate the scale to fit the image within the PDF page
        page_width, page_height = letter
        scale = min(page_width / img_width, page_height / img_height)
        scaled_width = img_width * scale
        scaled_height = img_height * scale

        # Center the image on the page
        x = (page_width - scaled_width) / 2
        y = (page_height - scaled_height) / 2

        # Draw the image on the PDF page
        c.drawImage(img_path, x, y, width=scaled_width, height=scaled_height)

        # Add a new page
        c.showPage()

    # Save the PDF
    c.save()
    print(f"Poetry book created successfully: {output_pdf}")


# Define the folder containing the images and the output PDF file name
images_folder = '/home/jasvir/Music/book/'
output_pdf = '/home/jasvir/Music/book/poetry_book.pdf'

# Create the poetry book
create_poetry_book(images_folder, output_pdf)
