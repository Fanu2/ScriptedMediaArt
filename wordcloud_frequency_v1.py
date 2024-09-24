"""
Using Frequency
===============

Generate a word cloud using a dictionary of word frequency.
"""

import multidict as multidict
import numpy as np
import os
import re
from PIL import Image
from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def get_frequency_dict_for_text(sentence):
    """
    Creates a frequency dictionary from the given text.

    :param sentence: Input text
    :return: A MultiDict with word frequencies
    """
    full_terms_dict = multidict.MultiDict()
    tmp_dict = {}

    # Creating dict for counting frequencies
    for word in sentence.split():
        # Skip common stopwords
        if re.match(r"\b(a|the|an|to|in|for|of|or|by|with|is|on|that|be)\b", word, re.IGNORECASE):
            continue
        word = word.lower()
        tmp_dict[word] = tmp_dict.get(word, 0) + 1

    for key, value in tmp_dict.items():
        full_terms_dict.add(key, value)

    return full_terms_dict

def make_image(frequency_dict):
    """
    Generates and displays a word cloud image based on the given frequency dictionary.

    :param frequency_dict: A dictionary with word frequencies
    """
    alice_mask = np.array(Image.open("/home/jasvir/Pictures/word cloud/alice_mask.png"))

    wc = WordCloud(background_color="white", max_words=1000, mask=alice_mask)
    wc.generate_from_frequencies(frequency_dict)

    # Display the word cloud
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()

# Define the data directory
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the input text
with open(path.join(d, '/home/jasvir/Pictures/word cloud/triza.txt'), encoding='utf-8') as file:
    text = file.read()

# Generate and display the word cloud
make_image(get_frequency_dict_for_text(text))
