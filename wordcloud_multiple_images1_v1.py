#!/usr/bin/env python

import os
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

# Define the paths
text_file_path = '/home/jasvir/Pictures/word cloud/jodha.txt'
output_dir = '/home/jasvir/Pictures/word cloud/jodha/'

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Read the whole text
with open(text_file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Define different styles
styles = [
    {"background_color": "white", "max_words": 200, "colormap": "viridis"},
    {"background_color": "black", "max_words": 300, "colormap": "plasma"},
    {"background_color": "white", "max_words": 200, "colormap": "inferno"},
    {"background_color": "black", "max_words": 300, "colormap": "magma"},
    {"background_color": "white", "max_words": 200, "colormap": "cividis"},
    {"background_color": "black", "max_words": 300, "colormap": "cool"},
    {"background_color": "white", "max_words": 200, "colormap": "hot"},
    {"background_color": "black", "max_words": 300, "colormap": "spring"},
    {"background_color": "white", "max_words": 200, "colormap": "summer"},
    {"background_color": "black", "max_words": 300, "colormap": "autumn"},
]

# Generate and save word clouds
for i, style in enumerate(styles):
    wc = WordCloud(
        background_color=style["background_color"],
        max_words=style["max_words"],
        colormap=style["colormap"],
        stopwords=STOPWORDS
    ).generate(text)

    # Display the word cloud
    plt.figure()
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.title(f'Word Cloud {i + 1}')
    plt.show()

    # Save the word cloud after displaying
    output_file_path = path.join(output_dir, f'word_cloud_{i + 1}.png')
    wc.to_file(output_file_path)
    print(f'Saved word cloud {i + 1} to {output_file_path}')

print("All word clouds have been saved successfully.")
