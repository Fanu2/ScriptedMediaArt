"""
Image-Colored Wordcloud with Boundary Map
=========================================
A slightly more elaborate version of an image-colored wordcloud
that also takes edges in the image into account.
Recreating an image similar to the parrot example.
"""

import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_gradient_magnitude
from wordcloud import WordCloud, ImageColorGenerator

# Define the directory containing the files
d = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Load the text for the wordcloud
text = open(os.path.join(d, '/home/jasvir/Pictures/word cloud/poems.txt'), encoding="utf-8").read()

# Load the image and process it
parrot_color = np.array(Image.open(os.path.join(d, "/home/jasvir/Pictures/word cloud/parrot-by-jose-mari-gimenez2.jpg")))
parrot_color = parrot_color[::3, ::3]  # Subsample for performance

# Create a mask for the wordcloud
parrot_mask = parrot_color.copy()
parrot_mask[parrot_mask.sum(axis=2) == 0] = 255  # Set background to white

# Perform edge detection for better color boundaries
edges = np.mean([
    gaussian_gradient_magnitude(parrot_color[:, :, i] / 255., 2)
    for i in range(3)
], axis=0)
parrot_mask[edges > 0.08] = 255

# Create the wordcloud
wc = WordCloud(
    max_words=2000,
    mask=parrot_mask,
    max_font_size=40,
    random_state=42,
    relative_scaling=0
)

# Generate and recolor the wordcloud
wc.generate(text)
image_colors = ImageColorGenerator(parrot_color)
wc.recolor(color_func=image_colors)

# Save and display the wordcloud
output_path = os.path.join(d, "parrot_new.png")
wc.to_file(output_path)

# Plot the results
plt.figure(figsize=(10, 10))
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.title("Wordcloud with Image Coloring")
plt.show()

plt.figure(figsize=(10, 10))
plt.title("Original Image")
plt.imshow(parrot_color)
plt.axis("off")
plt.show()

plt.figure(figsize=(10, 10))
plt.title("Edge Map")
plt.imshow(edges, cmap="gray")
plt.axis("off")
plt.show()
