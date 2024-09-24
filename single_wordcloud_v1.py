"""
Single Word Wordcloud
======================
Create a word cloud with a single word that's repeated.
"""

import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Define the text for the wordcloud
text = "Happy Anniversary Gurveer Haqumat"

# Create a mask for the wordcloud
x, y = np.ogrid[:300, :300]
mask = (x - 150) ** 2 + (y - 150) ** 2 > 130 ** 2
mask = 255 * mask.astype(int)

# Create the wordcloud
wc = WordCloud(
    background_color="white",
    repeat=True,
    mask=mask
)
wc.generate(text)

# Display the wordcloud
plt.figure(figsize=(8, 8))
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.title("Single Word Wordcloud")
plt.show()
