#!/usr/bin/env python
"""
Using custom colors for word cloud
==================================
Using the recolor method and custom coloring functions.
"""

import numpy as np
from PIL import Image
from os import path
import matplotlib.pyplot as plt
import random
from wordcloud import WordCloud, STOPWORDS

def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    """Custom color function to generate shades of grey."""
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

# Define the data directory
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Load the mask image
mask = np.array(Image.open(path.join(d, "/home/jasvir/Pictures/word cloud/fanu.png")))

# Read the text file
with open(path.join(d, '/home/jasvir/Pictures/word cloud/poems.txt'), 'r', encoding='utf-8') as file:
    text = file.read()

# Pre-process the text
text = text.replace("HAN", "Han").replace("LUKE'S", "Luke")

# Define custom stopwords
stopwords = set(STOPWORDS)
stopwords.update(["int", "ext"])

# Generate the word cloud
wc = WordCloud(
    max_words=1000,
    mask=mask,
    stopwords=stopwords,
    margin=10,
    random_state=1
).generate(text)

# Store the default colored image
default_colors = wc.to_array()

# Display the custom colored word cloud
plt.figure(figsize=(10, 10))
plt.title("Custom colors")
plt.imshow(wc.recolor(color_func=grey_color_func, random_state=3), interpolation="bilinear")
wc.to_file("a_new_hope_custom.png")
plt.axis("off")

# Display the default colored word cloud
plt.figure(figsize=(10, 10))
plt.title("Default colors")
plt.imshow(default_colors, interpolation="bilinear")
plt.axis("off")

# Show plots
plt.show()
