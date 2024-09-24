#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SlideShare Downloader and PDF Generator

Usage:
    slideshare_downloader.py
"""

import os
import img2pdf
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup


class SlideShareDownloader:
    """Download slides from SlideShare and convert them into a PDF."""

    def __init__(self, output_path='/home/jasvir/Pictures/Slideshare/'):
        self.output_path = output_path
        self.image_dir = os.path.join(self.output_path, 'images')

        if not os.path.exists(self.output_path):
            print(f"Output path '{self.output_path}' does not exist. Please create the directory first.")
            exit()

        if not os.path.exists(self.image_dir):
            os.makedirs(self.image_dir)

    def get_slides(self):
        download_url = input('Enter SlideShare full URL (including "https://"): ')
        output_filename = input('Enter the output filename (without extension): ')

        image_dir = self.download_images(download_url)
        if image_dir:
            self.create_pdf(image_dir, os.path.join(self.output_path, output_filename + '.pdf'))
        else:
            print("No images found. PDF creation failed.")

    def download_images(self, page_url):
        try:
            html = requests.get(page_url).text
            soup = BeautifulSoup(html, 'html.parser')

            # Print out the page source for debugging
            print("Page source fetched for debugging.")
            print(soup.prettify())

            # Update the class name or add new selectors based on the actual SlideShare page
            images = soup.findAll('img')  # General tag search for all image formats

            if not images:
                print("No images found with the specified class name.")
                return None

            for i, image in enumerate(images):
                image_url = image.get('data-full') or image.get('src')
                if image_url:
                    image_url = image_url.split('?')[0]
                    image_extension = os.path.splitext(urlparse(image_url).path)[1]
                    image_filename = f"slide_{i + 1}{image_extension}"
                    file_path = os.path.join(self.image_dir, image_filename)

                    print(f"Downloading {image_url}")  # Debug print
                    response = requests.get(image_url)
                    with open(file_path, "wb") as file:
                        file.write(response.content)

            return self.image_dir

        except Exception as e:
            print(f"Error downloading images: {e}")
            return None

    def create_pdf(self, image_dir, filename):
        try:
            files = [os.path.join(image_dir, file) for file in os.listdir(image_dir) if
                     file.endswith(('jpg', 'jpeg', 'png', 'svg'))]

            if not files:
                print("No image files found to create a PDF.")
                return

            with open(filename, "wb") as file:
                img2pdf.convert(*files, outputstream=file)

            print(f"PDF created successfully at {filename}")

        except Exception as e:
            print(f"Error creating PDF: {e}")


if __name__ == "__main__":
    downloader = SlideShareDownloader()
    downloader.get_slides()
