#!/usr/bin/env python
"""
Word Cloud Generator
====================

Generates and displays word clouds from a given text file.
"""

import os
from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def generate_wordcloud(file_path):
    """
    Generates and displays a word cloud from the text file at the given path.
    """
    # Check if file exists
    if not path.isfile(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    # Read the entire text from the file
    with open(file_path, 'r') as file:
        text = file.read()

    # Generate a word cloud image
    wordcloud = WordCloud().generate(text)

    # Display the generated image using matplotlib
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.title("Papa")
    plt.show()

    # Generate and display a word cloud with a lower maximum font size
    wordcloud = WordCloud(max_font_size=40).generate(text)
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.title("Word Cloud with Lower Max Font Size")
    plt.show()


if __name__ == "__main__":
    # Get the data directory
    d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

    # Define the path to the text file
    text_file_path = path.join(d, '/home/jasvir/Pictures/txt/poems.txt')

    try:
        generate_wordcloud(text_file_path)
    except Exception as e:
        print(f"An error occurred: {e}")
