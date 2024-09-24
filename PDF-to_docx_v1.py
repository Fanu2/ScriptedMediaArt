from pdf2docx import Converter
import os

# Paths
pdf_path = '/home/jasvir/Documents/Princess Rosa/PDF/fanu50.pdf'
docx_path = '/home/jasvir/Documents/Princess Rosa/PDF/fanu50.docx'


def convert_pdf_to_docx(pdf_file, docx_file):
    # Create a converter object
    converter = Converter(pdf_file)

    # Convert PDF to DOCX
    converter.convert(docx_file, start=0, end=None)

    # Close the converter
    converter.close()

    print(f"Conversion completed: {pdf_file} to {docx_file}")


if __name__ == "__main__":
    convert_pdf_to_docx(pdf_path, docx_path)
