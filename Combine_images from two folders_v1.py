from PIL import Image
import os
import random

# Define paths
images_dir1 = "/home/jasvir/Music/Jodha3/circular/"
images_dir2 = "/home/jasvir/Music/Jodha3/images/circular/"
output_dir = "/home/jasvir/Music/Jodha3/images/circular/combined_images/"

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Get list of images from both directories
images_list1 = [f for f in os.listdir(images_dir1) if os.path.isfile(os.path.join(images_dir1, f))]
images_list2 = [f for f in os.listdir(images_dir2) if os.path.isfile(os.path.join(images_dir2, f))]

# Limit the number of pairs to the number of images in images_dir1
num_pairs = min(len(images_list1), len(images_list2))

# Shuffle images in both lists
random.shuffle(images_list1)
random.shuffle(images_list2)

# Combine images and save
for i in range(num_pairs):
    # Open images
    img1_path = os.path.join(images_dir1, images_list1[i])
    img2_path = os.path.join(images_dir2, images_list2[i])

    img1 = Image.open(img1_path)
    img2 = Image.open(img2_path)

    # Calculate size for combined image
    width1, height1 = img1.size
    width2, height2 = img2.size
    combined_width = width1 + width2
    combined_height = max(height1, height2)

    # Create a new image with combined size
    combined_img = Image.new('RGB', (combined_width, combined_height), 'white')

    # Paste images into the combined image
    combined_img.paste(img1, (0, 0))
    combined_img.paste(img2, (width1, 0))

    # Save the combined image
    combined_img_filename = os.path.join(output_dir, f"combined_{i + 1}.png")
    combined_img.save(combined_img_filename)

    print(f"Combined image saved: {combined_img_filename}")

print("All combined images created successfully!")
