import pdfplumber  # For fetching text from PDF
from gtts import gTTS  # For converting text into mp3
import os
import time

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    raw_text = ""
    try:
        print(f"Opening PDF file: {pdf_path}")
        start_time = time.time()
        with pdfplumber.open(pdf_path) as pdf:
            total_pages = pdf.pages  # Get total pages in PDF
            print(f"Total pages: {len(total_pages)}")

            # Iterate over all pages to read text
            for i, page in enumerate(total_pages):
                print(f"Extracting text from page {i + 1}...")
                try:
                    text = page.extract_text()
                    if text:
                        raw_text += text
                    else:
                        print(f"No text found on page {i + 1}")
                except Exception as e:
                    print(f"Error extracting text from page {i + 1}: {e}")

        end_time = time.time()
        print(f"Text extraction completed in {end_time - start_time:.2f} seconds")
    except Exception as e:
        print(f"Error opening PDF file: {e}")
    return raw_text

def convert_text_to_audio(text, audio_path):
    """Convert text to audio and save it as an MP3 file."""
    try:
        if text.strip():  # Only create audio if text is not empty
            print(f"Converting text to audio...")
            start_time = time.time()
            gtts_obj = gTTS(text=text, lang="en")
            gtts_obj.save(audio_path)
            end_time = time.time()
            print(f"Audio saved as {audio_path} in {end_time - start_time:.2f} seconds")
        else:
            print("No text to convert to audio.")
    except Exception as e:
        print(f"Error saving audio file: {e}")

def main():
    # Fixed PDF path for testing
    pdf_path = "/home/jasvir/Documents/CliptoPDF/Fanu.pdf"

    if not os.path.isfile(pdf_path):
        print(f"PDF file not found at {pdf_path}")
        return

    # Extract text from PDF
    print(f"Extracting text from {pdf_path}...")
    text = extract_text_from_pdf(pdf_path)

    if not text:
        print("No text extracted from the PDF.")
        return

    print(f"Text extracted from {pdf_path}:\n{text[:1000]}...")  # Show only first 1000 characters for brevity

    # Get audio filename from user
    audio_filename = input("Enter the name of output file(without extension): ").strip()
    if not audio_filename:
        print("Audio filename cannot be empty.")
        return

    audio_path = f"{audio_filename}.mp3"

    # Convert text to audio
    print(f"Converting text to audio and saving as {audio_path}...")
    convert_text_to_audio(text, audio_path)

    print("Conversion done!")

if __name__ == "__main__":
    main()
