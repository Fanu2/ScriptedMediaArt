from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# Load the mask image
mask_image = Image.open('/home/jasvir/Pictures/fanu/fanu.png').convert('L')  # Convert image to grayscale

# Convert mask image to black and white with white background
mask_array = np.array(mask_image)
mask_array[mask_array < 128] = 0  # Convert dark areas to black
mask_array[mask_array >= 128] = 255  # Convert light areas to white
mask_image = Image.fromarray(mask_array)

# Create the word cloud
wordcloud = WordCloud(mask=np.array(mask_image), contour_color='black', contour_width=1).generate("Your text here")

# Display the word cloud
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
