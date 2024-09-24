from imagededup.methods import PHash
from imagededup.utils import plot_duplicates
import os

# Initialize PHash object
phasher = PHash()

# Directory containing images
image_dir = '/home/jasvir/Documents/Slide show2'

# Generate encodings
encodings = phasher.encode_images(image_dir=image_dir)

# Find duplicates
duplicates = phasher.find_duplicates(encoding_map=encodings)

# Print duplicates
print(duplicates)

# Visualize duplicates for each file that has duplicates
for filename, dup_list in duplicates.items():
    if dup_list:  # Only plot if there are duplicates
        output_plot = os.path.join(image_dir, f'duplicate_plot_{filename}.png')
        try:
            # Plot duplicates and save the plot
            plot_duplicates(image_dir=image_dir, duplicate_map=duplicates, filename=filename)
            # Save the plot to a file
            import matplotlib.pyplot as plt
            plt.savefig(output_plot)
            plt.close()
            print(f'Duplicate plot saved for {filename} at {output_plot}')
        except Exception as e:
            print(f'Error plotting duplicates for {filename}: {e}')
