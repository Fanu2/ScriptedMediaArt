#!/usr/bin/env python
"""
Masked WordCloud
================

Generates a word cloud in the shape of a mask image.
"""

import os
from os import path
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS


def generate_masked_wordcloud(text_file, mask_file, output_file):
    """
    Generates a word cloud image based on a text file and a mask image.

    :param text_file: Path to the input text file
    :param mask_file: Path to the mask image file
    :param output_file: Path to the output image file
    """
    # Get the directory of the script
    d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

    # Define file paths
    text_path = path.join(d, text_file)
    mask_path = path.join(d, mask_file)
    output_path = path.join(d, output_file)

    # Read the text file
    if not os.path.isfile(text_path):
        raise FileNotFoundError(f"The text file {text_path} does not exist.")
    with open(text_path, 'r') as file:
        text = file.read()

    # Read the mask image
    if not os.path.isfile(mask_path):
        raise FileNotFoundError(f"The mask image file {mask_path} does not exist.")
    alice_mask = np.array(Image.open(mask_path))

    # Define stopwords
    stopwords = set(STOPWORDS)
    stopwords.add("said")

    # Generate word cloud
    wc = WordCloud(
        background_color="white",
        max_words=2000,
        mask=alice_mask,
        stopwords=stopwords,
        contour_width=3,
        contour_color='steelblue'
    )
    wc.generate(text)

    # Save word cloud image to file
    wc.to_file(output_path)

    # Display the word cloud and the mask
    plt.figure(figsize=(10, 8))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.title("Word Cloud")
    plt.figure(figsize=(10, 8))
    plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
    plt.axis("off")
    plt.title("Mask Image")
    plt.show()


if __name__ == "__main__":
    # Define file names
    text_file = '/home/jasvir/Pictures/txt/triza.txt'
    mask_file = '/home/jasvir/Pictures/txt/alice_mask.png'
    output_file = '/home/jasvir/Pictures/txt/triza.png'

    try:
        generate_masked_wordcloud(text_file, mask_file, output_file)
        print(f"Word cloud generated and saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")
