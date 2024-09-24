import cv2
import numpy as np
import os

# Define parameters
TILE_WIDTH = 256
TILE_HEIGHT = 256
OVERLAP = False
IMAGE_PATH = '/home/jasvir/Pictures/Jodha2/2.jpg'
OUTPUT_FOLDER = '/home/jasvir/Pictures/Jodha2/'

def read_image(image_path):
    """Read the image from the specified path."""
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Image not found at {image_path}")
    return img

def create_tiles(img, tile_width, tile_height, overlap=False):
    """Create tiles from the image."""
    tiles = []
    img_height, img_width, _ = img.shape

    step_x = tile_width if not overlap else tile_width // 2
    step_y = tile_height if not overlap else tile_height // 2

    for y in range(0, img_height, step_y):
        for x in range(0, img_width, step_x):
            tile = img[y:y + tile_height, x:x + tile_width]

            # Adjust tile size if it extends beyond the image boundaries
            if tile.shape[0] < tile_height or tile.shape[1] < tile_width:
                tile = img[y:min(y + tile_height, img_height), x:min(x + tile_width, img_width)]

            tiles.append(tile)
    return tiles

def save_tiles(tiles, output_folder):
    """Save the tiles to the specified output folder."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for i, tile in enumerate(tiles):
        filename = os.path.join(output_folder, f'tile_{i}.png')
        cv2.imwrite(filename, tile)

def main():
    """Main function to run the tile creation process."""
    img = read_image(IMAGE_PATH)
    tiles = create_tiles(img, TILE_WIDTH, TILE_HEIGHT, OVERLAP)
    save_tiles(tiles, OUTPUT_FOLDER)
    print(f"Tiles created and saved to {OUTPUT_FOLDER}")

if __name__ == "__main__":
    main()
