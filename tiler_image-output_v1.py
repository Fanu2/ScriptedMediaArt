import cv2
import numpy as np
import os
import sys
from collections import defaultdict
from tqdm import tqdm
from multiprocessing import Pool
import math
import pickle
from time import sleep
import conf

# Configuration constants
COLOR_DEPTH = conf.COLOR_DEPTH
IMAGE_SCALE = conf.IMAGE_SCALE
RESIZING_SCALES = conf.RESIZING_SCALES
PIXEL_SHIFT = conf.PIXEL_SHIFT
POOL_SIZE = conf.POOL_SIZE
OVERLAP_TILES = conf.OVERLAP_TILES

def color_quantization(img, n_colors):
    """Reduces the number of colors in an image."""
    return np.round(img / 255 * n_colors) / n_colors * 255


def read_image(path, mainImage=False):
    img = cv2.imread(path, cv2.IMREAD_UNCHANGED)

    if img is None:
        raise ValueError(f"Image not found or unable to load at path {path}")

    # Check the number of channels in the image
    if len(img.shape) == 2:  # Grayscale image
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGRA)  # Convert to BGRA
    elif len(img.shape) == 3 and img.shape[2] == 3:  # RGB image
        img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)  # Convert to BGRA

    img = color_quantization(img.astype('float'), COLOR_DEPTH)

    # Scale the image according to IMAGE_SCALE, if this is the main image
    if mainImage:
        img = cv2.resize(img, (0, 0), fx=IMAGE_SCALE, fy=IMAGE_SCALE)

    return img.astype('uint8')


def resize_image(img, ratio):
    """Scales an image."""
    return cv2.resize(img, (int(img.shape[1] * ratio), int(img.shape[0] * ratio)))

def mode_color(img, ignore_alpha=False):
    """Returns the most frequent color in an image and its relative frequency."""
    counter = defaultdict(int)
    total = 0
    for y in img:
        for x in y:
            if len(x) < 4 or ignore_alpha or x[3] != 0:
                counter[tuple(x[:3])] += 1
            else:
                counter[(-1, -1, -1)] += 1
            total += 1
    if total > 0:
        mode_color = max(counter, key=counter.get)
        if mode_color == (-1, -1, -1):
            return None, None
        else:
            return mode_color, counter[mode_color] / total
    else:
        return None, None

def show_image(img, wait=True):
    """Displays an image."""
    cv2.imshow('img', img)
    cv2.waitKey(0 if wait else 1)

def load_tiles(paths):
    """Load and process the tiles."""
    print('Loading tiles')
    tiles = defaultdict(list)
    for path in paths:
        if os.path.isdir(path):
            for tile_name in tqdm(os.listdir(path)):
                tile = read_image(os.path.join(path, tile_name))
                mode, rel_freq = mode_color(tile, ignore_alpha=True)
                if mode is not None:
                    for scale in RESIZING_SCALES:
                        t = resize_image(tile, scale)
                        res = tuple(t.shape[:2])
                        tiles[res].append({'tile': t, 'mode': mode, 'rel_freq': rel_freq})
            with open('tiles.pickle', 'wb') as f:
                pickle.dump(tiles, f)
        else:
            with open(path, 'rb') as f:
                tiles = pickle.load(f)
    return tiles

def image_boxes(img, res):
    """Returns the boxes (image and start pos) from an image, with 'res' resolution."""
    shift = PIXEL_SHIFT if PIXEL_SHIFT else np.flip(res)
    boxes = [{'img': img[y:y + res[0], x:x + res[1]], 'pos': (x, y)}
             for y in range(0, img.shape[0], shift[1])
             for x in range(0, img.shape[1], shift[0])]
    return boxes

def color_distance(c1, c2):
    """Euclidean distance between two colors."""
    return math.sqrt(sum((int(a) - int(b)) ** 2 for a, b in zip(c1, c2)))

def most_similar_tile(box_mode_freq, tiles):
    """Returns the most similar tile to a box (in terms of color)."""
    if not box_mode_freq[0]:
        return 0, np.zeros(shape=tiles[0]['tile'].shape)
    min_distance = float('inf')
    min_tile_img = None
    for t in tiles:
        dist = (1 + color_distance(box_mode_freq[0], t['mode'])) / box_mode_freq[1]
        if dist < min_distance:
            min_distance = dist
            min_tile_img = t['tile']
    return min_distance, min_tile_img

def get_processed_image_boxes(image_path, tiles):
    """Builds the boxes and finds the best tile for each one."""
    print('Getting and processing boxes')
    img = read_image(image_path, mainImage=True)
    pool = Pool(POOL_SIZE)
    all_boxes = []

    for res, ts in tqdm(sorted(tiles.items(), reverse=True)):
        boxes = image_boxes(img, res)
        modes = pool.map(mode_color, [x['img'] for x in boxes])
        most_similar_tiles = pool.starmap(most_similar_tile, zip(modes, [ts] * len(modes)))

        for i, (min_dist, tile) in enumerate(most_similar_tiles):
            boxes[i]['min_dist'] = min_dist
            boxes[i]['tile'] = tile

        all_boxes.extend(boxes)

    return all_boxes, img.shape

def place_tile(img, box):
    """Places a tile in the image."""
    p1 = np.flip(box['pos'])
    p2 = p1 + box['img'].shape[:2]
    img_box = img[p1[0]:p2[0], p1[1]:p2[1]]
    mask = box['tile'][:, :, 3] != 0
    mask = mask[:img_box.shape[0], :img_box.shape[1]]
    if OVERLAP_TILES or not np.any(img_box[mask]):
        img_box[mask] = box['tile'][:img_box.shape[0], :img_box.shape[1], :][mask]

def create_tiled_image(boxes, res, render=False):
    """Tiles the image."""
    print('Creating tiled image')
    img = np.zeros(shape=(res[0], res[1], 4), dtype=np.uint8)
    for box in tqdm(sorted(boxes, key=lambda x: x['min_dist'], reverse=OVERLAP_TILES)):
        place_tile(img, box)
        if render:
            show_image(img, wait=False)
            sleep(0.025)
    return img

def main():
    """Main function."""
    image_path = sys.argv[1] if len(sys.argv) > 1 else conf.IMAGE_TO_TILE
    tiles_paths = sys.argv[2:] if len(sys.argv) > 2 else conf.TILES_FOLDER.split(' ')

    if not os.path.exists(image_path):
        print('Image not found')
        exit(-1)
    for path in tiles_paths:
        if not os.path.exists(path):
            print('Tiles folder not found')
            exit(-1)

    tiles = load_tiles(tiles_paths)
    boxes, original_res = get_processed_image_boxes(image_path, tiles)
    img = create_tiled_image(boxes, original_res, render=conf.RENDER)
    cv2.imwrite(conf.OUT, img)

if __name__ == "__main__":
    main()
